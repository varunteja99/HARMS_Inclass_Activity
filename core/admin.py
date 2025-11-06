from django.contrib import admin
from .models import (
    User, Patient, Doctor, SystemAdmin,
    MedicalRecord, Appointment, Notification,
    Schedule, Analytics, Report,
    Medication, TestResult, TimeSlot
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'user_type', 'is_active')
    list_filter = ('user_type', 'is_active')
    search_fields = ('email', 'user_id')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'full_name', 'email', 'phone_number')
    search_fields = ('patient_id', 'full_name', 'email')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'full_name', 'specialty', 'department')
    search_fields = ('doctor_id', 'full_name', 'specialty')


@admin.register(SystemAdmin)
class SystemAdminAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'full_name', 'access_level')
    search_fields = ('admin_id', 'full_name')


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'patient_id', 'doctor_id', 'visit_date')
    list_filter = ('visit_date', 'visit_type')
    search_fields = ('record_id', 'patient_id', 'doctor_id')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'patient_id', 'doctor_id', 'appointment_date', 'status')
    list_filter = ('status', 'specialty', 'appointment_date')
    search_fields = ('appointment_id', 'patient_id', 'doctor_id')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'user_id', 'type', 'priority', 'is_read', 'sent_date')
    list_filter = ('type', 'priority', 'is_read', 'sent_date')
    search_fields = ('notification_id', 'user_id', 'message')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule_id', 'doctor_id', 'start_time', 'end_time')
    search_fields = ('schedule_id', 'doctor_id')


@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('analytics_id', 'metric_type', 'value')
    search_fields = ('analytics_id', 'metric_type')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'report_type', 'generated_date', 'generated_by')
    list_filter = ('report_type', 'generated_date')
    search_fields = ('report_id', 'generated_by')


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('medication_id', 'name', 'dosage', 'prescribed_date')
    search_fields = ('medication_id', 'name')


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('test_id', 'test_name', 'test_date', 'status')
    list_filter = ('test_date', 'status')
    search_fields = ('test_id', 'test_name')


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id', 'start_time', 'end_time', 'is_available')
    list_filter = ('is_available', 'start_time')
    search_fields = ('slot_id',)