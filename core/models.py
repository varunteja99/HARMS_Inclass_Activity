from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator
from datetime import datetime, date
from typing import List, Optional
from .enums import (
    UserType, Priority, NotificationType, 
    AppointmentStatus, ReportType
)


class UserManager(BaseUserManager):
    """Custom user manager"""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Base User class"""
    user_id = models.CharField(max_length=100, unique=True)  # Remove primary_key=True
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    user_type = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in UserType]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    objects = UserManager()

    def login(self) -> bool:
        """Login method"""
        return True

    def logout(self) -> None:
        """Logout method"""
        pass

    def register(self) -> bool:
        """Register method"""
        return True

    def update_profile(self) -> bool:
        """Update profile method"""
        return True

    def reset_password(self) -> bool:
        """Reset password method"""
        return True

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Patient(User):
    """Patient class inheriting from User"""
    # Remove primary_key=True from patient_id
    patient_id = models.CharField(max_length=100, unique=True)  # Remove primary_key=True
    full_name = models.CharField(max_length=200)
    insurance_info = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def view_medical_records(self) -> List['MedicalRecord']:
        """View medical records"""
        return list(MedicalRecord.objects.filter(patient_id=self.patient_id))

    def book_appointment(self) -> 'Appointment':
        """Book appointment"""
        # Implementation would create and return an appointment
        pass

    def manage_appointments(self) -> None:
        """Manage appointments"""
        pass

    def view_profile(self):
        """View profile"""
        return {
            'patient_id': self.patient_id,
            'full_name': self.full_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address
        }

    def update_profile(self) -> bool:
        """Update profile"""
        return super().update_profile()

    class Meta:
        db_table = 'patients'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Doctor(User):
    """Doctor class inheriting from User"""
    doctor_id = models.CharField(max_length=100, unique=True)  # Remove primary_key=True
    full_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)

    def view_schedule(self) -> List['Appointment']:
        """View schedule"""
        return list(Appointment.objects.filter(doctor_id=self.doctor_id))

    def manage_patient_records(self) -> None:
        """Manage patient records"""
        pass

    def update_medical_records(self) -> bool:
        """Update medical records"""
        return True

    def set_availability(self) -> bool:
        """Set availability"""
        return True

    def process_appointment(self) -> None:
        """Process appointment"""
        pass

    class Meta:
        db_table = 'doctors'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class SystemAdmin(User):
    """SystemAdmin class inheriting from User"""
    admin_id = models.CharField(max_length=100, unique=True)  # Remove primary_key=True
    full_name = models.CharField(max_length=200)
    access_level = models.CharField(max_length=50)

    def generate_reports(self) -> 'Report':
        """Generate reports"""
        pass

    def manage_users(self) -> None:
        """Manage users"""
        pass

    def view_analytics(self) -> 'Analytics':
        """View analytics"""
        pass

    def system_settings(self) -> None:
        """System settings"""
        pass

    def backup_database(self) -> bool:
        """Backup database"""
        return True

    class Meta:
        db_table = 'system_admins'
        verbose_name = 'System Admin'
        verbose_name_plural = 'System Admins'


class Medication(models.Model):
    """Medication class"""
    medication_id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    prescribed_date = models.DateField(default=date.today)

    def prescribe(self) -> bool:
        """Prescribe medication"""
        return True

    def refill(self) -> bool:
        """Refill medication"""
        return True

    class Meta:
        db_table = 'medications'
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'


class TestResult(models.Model):
    """TestResult class"""
    test_id = models.CharField(max_length=100, unique=True, primary_key=True)
    test_name = models.CharField(max_length=200)
    test_date = models.DateField(default=date.today)
    results = models.TextField()
    status = models.CharField(max_length=50)
    normal_ranges = models.TextField(blank=True, null=True)

    def upload(self) -> bool:
        """Upload test result"""
        return True

    def view(self):
        """View test result"""
        return {
            'test_id': self.test_id,
            'test_name': self.test_name,
            'test_date': self.test_date,
            'results': self.results,
            'status': self.status
        }

    class Meta:
        db_table = 'test_results'
        verbose_name = 'Test Result'
        verbose_name_plural = 'Test Results'
 

class TimeSlot(models.Model):
    """TimeSlot class"""
    slot_id = models.CharField(max_length=100, unique=True, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)

    def check_availability(self) -> bool:
        """Check availability"""
        return self.is_available

    def reserve(self) -> bool:
        """Reserve time slot"""
        if self.is_available:
            self.is_available = False
            self.save()
            return True
        return False

    def release(self) -> bool:
        """Release time slot"""
        self.is_available = True
        self.save()
        return True

    class Meta:
        db_table = 'time_slots'
        verbose_name = 'Time Slot'
        verbose_name_plural = 'Time Slots'


class MedicalRecord(models.Model):
    """MedicalRecord class"""
    record_id = models.CharField(max_length=100, unique=True, primary_key=True)
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
    visit_date = models.DateField(default=date.today)
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    medications = models.ManyToManyField(Medication, related_name='medical_records')
    test_results = models.ManyToManyField(TestResult, related_name='medical_records')
    visit_type = models.CharField(max_length=100)

    def create(self) -> bool:
        """Create medical record"""
        return True

    def update(self) -> bool:
        """Update medical record"""
        return True

    def view(self):
        """View medical record"""
        return {
            'record_id': self.record_id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'visit_date': self.visit_date,
            'diagnosis': self.diagnosis,
            'treatment_plan': self.treatment_plan
        }

    def download(self):
        """Download medical record"""
        # Implementation would return a file
        pass

    def add_test_result(self) -> bool:
        """Add test result"""
        return True

    class Meta:
        db_table = 'medical_records'
        verbose_name = 'Medical Record'
        verbose_name_plural = 'Medical Records'


class Schedule(models.Model):
    """Schedule class"""
    schedule_id = models.CharField(max_length=100, unique=True, primary_key=True)
    doctor_id = models.CharField(max_length=100)
    working_days = models.JSONField(default=list)  # List of day names
    start_time = models.TimeField()
    end_time = models.TimeField()
    available_slots = models.ManyToManyField(TimeSlot, related_name='schedules', blank=True)
    blocked_slots = models.ManyToManyField(TimeSlot, related_name='blocked_schedules', blank=True)

    def set_availability(self) -> bool:
        """Set availability"""
        return True

    def block_time_slot(self) -> bool:
        """Block time slot"""
        return True

    def get_available_slots(self) -> List[TimeSlot]:
        """Get available slots"""
        return list(self.available_slots.filter(is_available=True))

    def update_schedule(self) -> bool:
        """Update schedule"""
        return True

    class Meta:
        db_table = 'schedules'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'


class Appointment(models.Model):
    """Appointment class"""
    appointment_id = models.CharField(max_length=100, unique=True, primary_key=True)
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='appointments')
    specialty = models.CharField(max_length=100)
    reason_for_visit = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in AppointmentStatus],
        default=AppointmentStatus.PENDING.value
    )
    notes = models.TextField(blank=True, null=True)

    def create(self) -> bool:
        """Create appointment"""
        return True

    def reschedule(self) -> bool:
        """Reschedule appointment"""
        return True

    def cancel(self) -> bool:
        """Cancel appointment"""
        self.status = AppointmentStatus.CANCELLED.value
        self.save()
        return True

    def confirm(self) -> bool:
        """Confirm appointment"""
        self.status = AppointmentStatus.CONFIRMED.value
        self.save()
        return True

    def mark_completed(self) -> None:
        """Mark appointment as completed"""
        self.status = AppointmentStatus.COMPLETED.value
        self.save()

    def get_details(self):
        """Get appointment details"""
        return {
            'appointment_id': self.appointment_id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'appointment_date': self.appointment_date,
            'status': self.status,
            'reason_for_visit': self.reason_for_visit
        }
    
class Notification(models.Model):
    """Notification class"""
    notification_id = models.CharField(max_length=100, unique=True, primary_key=True)
    user_id = models.CharField(max_length=100)
    type = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in NotificationType]
    )
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in Priority],
        default=Priority.MEDIUM.value
    )

    def send(self) -> bool:
        """Send notification"""
        return True

    def mark_as_read(self) -> None:
        """Mark notification as read"""
        self.is_read = True
        self.save()

    @staticmethod
    def get_notifications(user_id: str) -> List['Notification']:
        """Get notifications for a user"""
        return list(Notification.objects.filter(user_id=user_id))

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


class Analytics(models.Model):
    """Analytics class"""
    analytics_id = models.CharField(max_length=100, unique=True, primary_key=True)
    metric_type = models.CharField(max_length=100)
    value = models.TextField()
    period = models.JSONField(default=dict)  # DateRange as JSON

    def calculate_metrics(self) -> dict:
        """Calculate metrics"""
        return {
            'metric_type': self.metric_type,
            'value': self.value,
            'period': self.period
        }

    def visualize(self):
        """Visualize analytics"""
        # Implementation would return a chart
        pass

    class Meta:
        db_table = 'analytics'
        verbose_name = 'Analytics'
        verbose_name_plural = 'Analytics'


class Report(models.Model):
    """Report class"""
    report_id = models.CharField(max_length=100, unique=True, primary_key=True)
    report_type = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in ReportType]
    )
    generated_date = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    generated_by = models.CharField(max_length=100)

    def generate(self) -> bool:
        """Generate report"""
        return True

    def export(self):
        """Export report"""
        # Implementation would return a file
        pass

    def view(self):
        """View report"""
        return {
            'report_id': self.report_id,
            'report_type': self.report_type,
            'generated_date': self.generated_date,
            'data': self.data
        }

    class Meta:
        db_table = 'reports'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

