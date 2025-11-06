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
