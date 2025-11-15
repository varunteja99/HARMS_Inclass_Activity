from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta
import uuid

from .models import (
    Patient, Doctor, SystemAdmin, Appointment,
    MedicalRecord, TimeSlot, Schedule, Notification,
    Medication, TestResult, Report, Analytics
)
from .serializers import (
    PatientSerializer, DoctorSerializer, SystemAdminSerializer,
    AppointmentSerializer, MedicalRecordSerializer, TimeSlotSerializer,
    ScheduleSerializer, NotificationSerializer, MedicationSerializer,
    TestResultSerializer, ReportSerializer, AnalyticsSerializer
)
from .enums import AppointmentStatus, NotificationType, Priority


class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Patient operations
    Use cases: Patient registration, profile management, view appointments
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'patient_id'

    @action(detail=False, methods=['post'])
    def register(self, request):
        """Register a new patient"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            patient = serializer.save()
            return Response({
                'message': 'Patient registered successfully',
                'patient_id': patient.patient_id,
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def appointments(self, request, patient_id=None):
        """Get all appointments for a patient"""
        appointments = Appointment.objects.filter(patient_id=patient_id)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def medical_records(self, request, patient_id=None):
        """Get all medical records for a patient"""
        records = MedicalRecord.objects.filter(patient_id=patient_id)
        serializer = MedicalRecordSerializer(records, many=True)
        return Response(serializer.data)


class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Doctor operations
    Use cases: Doctor registration, schedule management, view patients
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'doctor_id'

    @action(detail=True, methods=['get'])
    def schedule(self, request, doctor_id=None):
        """Get doctor's schedule"""
        schedules = Schedule.objects.filter(doctor_id=doctor_id)
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_schedule(self, request, doctor_id=None):
        """Set doctor's schedule"""
        data = request.data.copy()
        data['doctor_id'] = doctor_id
        if 'schedule_id' not in data:
            data['schedule_id'] = f"SCH-{uuid.uuid4().hex[:8].upper()}"

        serializer = ScheduleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Schedule created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def appointments(self, request, doctor_id=None):
        """Get all appointments for a doctor"""
        appointments = Appointment.objects.filter(doctor_id=doctor_id)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Appointment operations
    Use cases: Book appointment, reschedule, cancel, confirm
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'appointment_id'

    def create(self, request):
        """Book a new appointment"""
        data = request.data.copy()
        if 'appointment_id' not in data:
            data['appointment_id'] = f"APT-{uuid.uuid4().hex[:8].upper()}"

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            appointment = serializer.save()

            # Create notification for patient
            Notification.objects.create(
                notification_id=f"NOT-{uuid.uuid4().hex[:8].upper()}",
                user_id=appointment.patient_id,
                type=NotificationType.APPOINTMENT_CONFIRMATION.value,
                message=f"Your appointment has been booked for {appointment.appointment_date}",
                priority=Priority.HIGH.value
            )

            return Response({
                'message': 'Appointment booked successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def confirm(self, request, appointment_id=None):
        """Confirm an appointment"""
        try:
            appointment = self.get_object()
            appointment.confirm()
            return Response({
                'message': 'Appointment confirmed',
                'status': appointment.status
            })
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def cancel(self, request, appointment_id=None):
        """Cancel an appointment"""
        try:
            appointment = self.get_object()
            appointment.cancel()
            appointment.time_slot.release()
            return Response({
                'message': 'Appointment cancelled',
                'status': appointment.status
            })
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def complete(self, request, appointment_id=None):
        """Mark appointment as completed"""
        try:
            appointment = self.get_object()
            appointment.mark_completed()
            return Response({
                'message': 'Appointment marked as completed',
                'status': appointment.status
            })
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)


class TimeSlotViewSet(viewsets.ModelViewSet):
    """
    ViewSet for TimeSlot operations
    Use cases: View available slots, reserve slots
    """
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    lookup_field = 'slot_id'

    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available time slots"""
        slots = TimeSlot.objects.filter(is_available=True)
        serializer = self.get_serializer(slots, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_slots(self, request):
        """Create multiple time slots for a date range"""
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        start_time = request.data.get('start_time', '09:00')
        end_time = request.data.get('end_time', '17:00')

        # Simple slot creation for prototype
        slots_created = []
        current_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

        while current_date <= end_date_obj:
            slot_id = f"TS-{uuid.uuid4().hex[:8].upper()}"
            slot = TimeSlot.objects.create(
                slot_id=slot_id,
                start_time=datetime.combine(current_date.date(), datetime.strptime(start_time, '%H:%M').time()),
                end_time=datetime.combine(current_date.date(), datetime.strptime(end_time, '%H:%M').time()),
                is_available=True
            )
            slots_created.append(slot.slot_id)
            current_date += timedelta(days=1)

        return Response({
            'message': f'{len(slots_created)} time slots created',
            'slot_ids': slots_created
        }, status=status.HTTP_201_CREATED)


class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
    ViewSet for MedicalRecord operations
    Use cases: Create records, view records, update records
    """
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    lookup_field = 'record_id'

    def create(self, request):
        """Create a new medical record"""
        data = request.data.copy()
        if 'record_id' not in data:
            data['record_id'] = f"MR-{uuid.uuid4().hex[:8].upper()}"

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            record = serializer.save()

            # Create notification
            Notification.objects.create(
                notification_id=f"NOT-{uuid.uuid4().hex[:8].upper()}",
                user_id=record.patient_id,
                type=NotificationType.TEST_RESULTS_AVAILABLE.value,
                message=f"New medical record created for your visit on {record.visit_date}",
                priority=Priority.MEDIUM.value
            )

            return Response({
                'message': 'Medical record created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Notification operations
    Use cases: View notifications, mark as read
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'notification_id'

    @action(detail=False, methods=['get'])
    def user_notifications(self, request):
        """Get notifications for a specific user"""
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'user_id parameter required'}, status=status.HTTP_400_BAD_REQUEST)

        notifications = Notification.objects.filter(user_id=user_id).order_by('-sent_date')
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def mark_read(self, request, notification_id=None):
        """Mark a notification as read"""
        try:
            notification = self.get_object()
            notification.mark_as_read()
            return Response({
                'message': 'Notification marked as read',
                'is_read': notification.is_read
            })
        except Notification.DoesNotExist:
            return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)


class ReportViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Report operations
    Use cases: Generate reports, view reports
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'report_id'

    @action(detail=False, methods=['post'])
    def generate(self, request):
        """Generate a new report"""
        data = request.data.copy()
        if 'report_id' not in data:
            data['report_id'] = f"RPT-{uuid.uuid4().hex[:8].upper()}"

        # For prototype, create simple report data
        report_type = data.get('report_type')
        if report_type == 'APPOINTMENT_STATISTICS':
            total_appointments = Appointment.objects.count()
            data['data'] = f"Total Appointments: {total_appointments}"
        elif report_type == 'PATIENT_DEMOGRAPHICS':
            total_patients = Patient.objects.count()
            data['data'] = f"Total Patients: {total_patients}"
        else:
            data['data'] = "Report data placeholder"

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Report generated successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnalyticsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Analytics operations
    Use cases: View system analytics and metrics
    """
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    lookup_field = 'analytics_id'

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        """Get dashboard analytics"""
        analytics_data = {
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'total_appointments': Appointment.objects.count(),
            'pending_appointments': Appointment.objects.filter(status=AppointmentStatus.PENDING.value).count(),
            'completed_appointments': Appointment.objects.filter(status=AppointmentStatus.COMPLETED.value).count(),
        }
        return Response(analytics_data)
