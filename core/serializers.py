from rest_framework import serializers
from .models import (
    User, Patient, Doctor, SystemAdmin, Appointment,
    MedicalRecord, TimeSlot, Schedule, Notification,
    Medication, TestResult, Report, Analytics
)
from .enums import UserType, AppointmentStatus, NotificationType, Priority, ReportType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'phone_number', 'date_of_birth', 'user_type', 'is_active', 'created_at']
        read_only_fields = ['created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'patient_id', 'full_name', 'email', 'phone_number',
                  'date_of_birth', 'insurance_info', 'emergency_contact', 'address',
                  'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        password = validated_data.pop('password', 'defaultpass123')
        validated_data['user_type'] = UserType.PATIENT.value
        patient = Patient.objects.create_user(**validated_data)
        patient.set_password(password)
        patient.save()
        return patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctor_id', 'full_name', 'email', 'phone_number',
                  'specialty', 'license_number', 'department', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        password = validated_data.pop('password', 'defaultpass123')
        validated_data['user_type'] = UserType.DOCTOR.value
        doctor = Doctor.objects.create_user(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor


class SystemAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAdmin
        fields = ['id', 'admin_id', 'full_name', 'email', 'access_level', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['slot_id', 'start_time', 'end_time', 'is_available']


class ScheduleSerializer(serializers.ModelSerializer):
    available_slots = TimeSlotSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = ['schedule_id', 'doctor_id', 'working_days', 'start_time',
                  'end_time', 'available_slots']


class AppointmentSerializer(serializers.ModelSerializer):
    time_slot = TimeSlotSerializer(read_only=True)
    time_slot_id = serializers.CharField(write_only=True)

    class Meta:
        model = Appointment
        fields = ['appointment_id', 'patient_id', 'doctor_id', 'appointment_date',
                  'time_slot', 'time_slot_id', 'specialty', 'reason_for_visit',
                  'status', 'notes']
        read_only_fields = ['status']

    def create(self, validated_data):
        time_slot_id = validated_data.pop('time_slot_id')
        time_slot = TimeSlot.objects.get(slot_id=time_slot_id)
        appointment = Appointment.objects.create(time_slot=time_slot, **validated_data)
        time_slot.reserve()
        return appointment


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['medication_id', 'name', 'dosage', 'frequency', 'duration', 'prescribed_date']


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ['test_id', 'test_name', 'test_date', 'results', 'status', 'normal_ranges']


class MedicalRecordSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True, read_only=True)
    test_results = TestResultSerializer(many=True, read_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['record_id', 'patient_id', 'doctor_id', 'visit_date',
                  'diagnosis', 'treatment_plan', 'medications', 'test_results', 'visit_type']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['notification_id', 'user_id', 'type', 'message',
                  'sent_date', 'is_read', 'priority']
        read_only_fields = ['sent_date']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['report_id', 'report_type', 'generated_date', 'data', 'generated_by']
        read_only_fields = ['generated_date']


class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = ['analytics_id', 'metric_type', 'value', 'period']
