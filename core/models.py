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
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=128)  # Will be hashed by Django
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
    patient_id = models.CharField(max_length=100, unique=True, primary_key=True)
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
    doctor_id = models.CharField(max_length=100, unique=True, primary_key=True)
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
    admin_id = models.CharField(max_length=100, unique=True, primary_key=True)
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
 
