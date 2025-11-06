# HARMS_Inclass_Activity

This repository contains the backend code of Healthcare Appointment and Record Management System (HARMS).

## Programming Language

**Python 3.11** with **Django 5.2.7** framework

We chose Python/Django for this project because:
- Django provides a robust ORM (Object-Relational Mapping) that makes it easy to translate UML class models into database models
- Django's model system supports inheritance, relationships, and all the UML concepts we need
- Python's clean syntax and Django's conventions align well with the UML class diagram structure
- Django provides built-in admin interface, authentication, and REST API capabilities for future development phases

## Class Models Location

All UML class models have been translated into Django models and are located in:

**`core/models.py`**

This file contains all the class models from the UML diagram:

### User Classes (Inheritance Hierarchy)
- `User` - Base user class with common attributes and methods
- `Patient` - Inherits from User
- `Doctor` - Inherits from User  
- `SystemAdmin` - Inherits from User

### Core Domain Models
- `MedicalRecord` - Patient medical records
- `Appointment` - Appointment management
- `Notification` - User notifications
- `Schedule` - Doctor schedules
- `Analytics` - System analytics
- `Report` - System reports

### Supporting Models
- `Medication` - Medication prescriptions
- `TestResult` - Medical test results
- `TimeSlot` - Available time slots for appointments

### Enumerations

All enumerations from the UML diagram are defined in:

**`core/enums.py`**

This file contains:
- `UserType` - PATIENT, DOCTOR, SYSTEM_ADMIN
- `Priority` - LOW, MEDIUM, HIGH, URGENT
- `NotificationType` - APPOINTMENT_CONFIRMATION, APPOINTMENT_REMINDER, TEST_RESULTS_AVAILABLE, PRESCRIPTION_RENEWAL, HEALTH_ALERT, SYSTEM_MAINTENANCE
- `AppointmentStatus` - PENDING, CONFIRMED, SCHEDULED, COMPLETED, CANCELLED
- `ReportType` - PATIENT_DEMOGRAPHICS, DOCTOR_UTILIZATION, APPOINTMENT_STATISTICS, REVENUE_ANALYSIS

## Implementation Status

**Week 1 - Implementation/Development - I:**
- ✅ Programming language chosen: Python/Django
- ✅ Development environment setup (Docker & Docker Compose)
- ✅ UML class models translated to Django models in `core/models.py`
- ✅ All enumerations defined in `core/enums.py`
- ✅ Basic programming standards applied (naming conventions, class structure, methods)

## Next Steps

- Week 2: Use case (sequence model) → Programming
- Week 3: Code refactoring
- Week 4: Testing (use case → test cases & test data)