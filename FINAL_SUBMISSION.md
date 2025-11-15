# HARMS - Healthcare Appointment and Record Management System
## Final Project Submission

---

## 📌 Project Information

**Course**: ACS 560 Software Engineering
**Team**: ACS 560_Project_Team_2
**Submission Date**: November 15, 2025

**Project Description**: A comprehensive healthcare management platform enabling patients to book appointments, view medical records, and receive notifications, while providing doctors with tools to manage patient records and schedules, and administrators with system analytics.

---

## 🔗 GitHub Repository Links

### Backend Repository (Django REST API)
**URL**: https://github.com/varunteja99/HARMS_Inclass_Activity

**Technology Stack**:
- Framework: Django 5.2.7
- REST API: Django REST Framework 3.16.1
- Database: PostgreSQL 15
- Caching: Redis 7
- Containerization: Docker & Docker Compose
- Language: Python 3.11

### Frontend Repository (React Application)
**URL**: https://github.com/varunteja99/HARMS_Inclass_Activity_Frontend

**Technology Stack**:
- Framework: React 18.2.0
- Routing: React Router DOM 6.20.0
- Build Tool: Vite 5.0.8
- HTTP Client: Axios 1.6.2
- Language: JavaScript (ES6+)

---

## 🎯 Use Case Implementation Status

### Summary
- **Total Use Cases Defined**: 12
- **Backend APIs Implemented**: 12/12 (100%)
- **Frontend Prototypes Implemented**: 5/12 (Key Use Cases)
- **Fully Functional & Tested**: 10/12 (83%)

---

## 📸 Use Case to Screenshot Mapping

### ✅ USE CASE 1: Register/Login (UC01)
**Actor**: Patient, Doctor, System Admin
**Status**: ✅ IMPLEMENTED (Backend + Frontend)

**Frontend Access**:
- **URL**: http://localhost:3000/login
- **Page**: Login/Register Interface

**Backend API**:
```bash
# Patient Registration
POST /api/patients/register/
Content-Type: application/json

{
  "patient_id": "PAT-1001",
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "phone_number": "+1-555-0123",
  "date_of_birth": "1990-05-15",
  "insurance_info": "Blue Cross Blue Shield - Policy #12345",
  "emergency_contact": "Jane Doe: +1-555-0124",
  "address": "123 Main St, Boston, MA 02101"
}
```

**Features Implemented**:
- User login with email and password
- New user registration
- User type selection (Patient/Doctor)
- Remember me functionality
- Form validation

**Screenshot Instructions**:
1. Navigate to http://localhost:3000/login
2. Fill in both login and register forms with sample data
3. Capture full-page screenshot showing both forms

**Project Outcome**: User authentication system with registration and login capabilities

---

### ✅ USE CASE 2: Manage Profile / Patient Dashboard (UC02)
**Actor**: Patient
**Status**: ✅ IMPLEMENTED (Backend + Frontend)

**Frontend Access**:
- **URL**: http://localhost:3000/dashboard
- **Page**: Patient Dashboard

**Backend API**:
```bash
# Get Patient Profile
GET /api/patients/{patient_id}/

# Update Patient Profile
PUT /api/patients/{patient_id}/
```

**Features Implemented**:
- Overview cards showing:
  - Upcoming Appointments count (3)
  - Medical Records count (12)
  - Unread Messages count (2)
- Profile Information display
- Next Appointment details
- Recent Notifications list
- Edit Profile functionality

**Screenshot Instructions**:
1. Navigate to http://localhost:3000/dashboard
2. Ensure all dashboard sections are visible
3. Capture full-page screenshot showing statistics, profile, appointment, and notifications

**Project Outcome**: Comprehensive patient dashboard with profile management and key metrics

---

### ✅ USE CASE 3: Book Appointment (UC03)
**Actor**: Patient
**Status**: ✅ IMPLEMENTED (Backend + Frontend)

**Frontend Access**:
- **URL**: http://localhost:3000/book-appointment
- **Page**: Book New Appointment

**Backend API**:
```bash
# Book Appointment
POST /api/appointments/
Content-Type: application/json

{
  "patient_id": "PAT-1001",
  "doctor_id": "DOC-2001",
  "appointment_date": "2025-11-16 10:00:00",
  "time_slot_id": "TS-12345678",
  "specialty": "Cardiology",
  "reason_for_visit": "Annual checkup and heart health consultation",
  "notes": "Patient has family history of heart disease"
}

# Get Available Time Slots
GET /api/time-slots/available/

# Create Time Slots
POST /api/time-slots/create_slots/
```

**Features Implemented**:
- Specialty selection dropdown (General Medicine, Cardiology, Dermatology)
- Doctor selection dropdown (filtered by specialty)
- Date picker for preferred appointment date
- Available time slots display (9:00 AM, 10:30 AM, 2:00 PM, 3:30 PM)
- Reason for visit text area
- Book Appointment and Cancel buttons

**Screenshot Instructions**:
1. Navigate to http://localhost:3000/book-appointment
2. Select specialty: "General Medicine"
3. Select doctor: "Dr. Sarah Johnson - General Medicine"
4. Choose a preferred date
5. Click on a time slot to select it (e.g., 10:30 AM)
6. Add reason for visit
7. Capture full-page screenshot

**Project Outcome**: Intuitive appointment booking system with specialty and time slot selection

---

### ✅ USE CASE 4: Manage Appointments (UC04)
**Actor**: Patient
**Status**: ✅ IMPLEMENTED (Backend + Frontend)

**Frontend Access**:
- **URL**: http://localhost:3000/manage-appointments
- **Page**: Manage Appointments

**Backend API**:
```bash
# View Patient Appointments
GET /api/patients/{patient_id}/appointments/

# Confirm Appointment
POST /api/appointments/{appointment_id}/confirm/

# Cancel Appointment
POST /api/appointments/{appointment_id}/cancel/
```

**Features Implemented**:
- Appointments table with columns:
  - Date & Time
  - Doctor Name
  - Specialty
  - Status (with colored badges)
  - Actions (Reschedule/Cancel buttons)
- Status indicators:
  - Confirmed (green badge)
  - Pending (orange badge)
  - Scheduled (blue badge)
- Reschedule functionality
- Cancel appointment functionality

**Sample Data Displayed**:
| Date & Time | Doctor | Specialty | Status | Actions |
|------------|--------|-----------|--------|---------|
| Mar 15, 2024 - 2:00 PM | Dr. Sarah Johnson | General Medicine | Confirmed | Reschedule / Cancel |
| Mar 22, 2024 - 10:30 AM | Dr. Michael Brown | Cardiology | Pending | Reschedule / Cancel |
| Apr 5, 2024 - 3:30 PM | Dr. Emily Davis | Dermatology | Scheduled | Reschedule / Cancel |

**Screenshot Instructions**:
1. Navigate to http://localhost:3000/manage-appointments
2. Ensure table displays all appointments with different statuses
3. Capture full-page screenshot showing the complete table

**Project Outcome**: Comprehensive appointment management interface with status tracking

---

### ✅ USE CASE 5: View Medical Records (UC05)
**Actor**: Patient
**Status**: ✅ IMPLEMENTED (Backend + Frontend)

**Frontend Access**:
- **URL**: http://localhost:3000/medical-records
- **Page**: Medical Records

**Backend API**:
```bash
# View Patient Medical Records
GET /api/patients/{patient_id}/medical_records/

# Create Medical Record
POST /api/medical-records/
Content-Type: application/json

{
  "patient_id": "PAT-1001",
  "doctor_id": "DOC-2001",
  "visit_date": "2025-11-14",
  "diagnosis": "Hypertension Stage 1",
  "treatment_plan": "Lifestyle modifications, regular monitoring",
  "visit_type": "Follow-up"
}
```

**Features Implemented**:
- **Recent Lab Results** section:
  - Date: March 10, 2024
  - Test: Complete Blood Count
  - Status: Normal ranges
  - View Details button
- **Current Medications** list:
  - Lisinopril 10mg - Once daily
  - Metformin 500mg - Twice daily
  - Vitamin D 1000IU - Once daily
  - Manage Medications button
- **Medical History** table:
  - Date
  - Doctor
  - Visit Type
  - Diagnosis
  - Actions (View Report button)

**Sample Data Displayed**:
| Date | Doctor | Visit Type | Diagnosis | Actions |
|------|--------|------------|-----------|---------|
| Mar 1, 2024 | Dr. Sarah Johnson | Annual Checkup | Hypertension, controlled | View Report |
| Dec 15, 2023 | Dr. Michael Brown | Cardiology Consultation | Normal EKG | View Report |

**Screenshot Instructions**:
1. Navigate to http://localhost:3000/medical-records
2. Ensure all three sections are visible:
   - Recent Lab Results
   - Current Medications
   - Medical History
3. Capture full-page screenshot

**Project Outcome**: Complete medical records interface with lab results, medications, and history

---

## 🔧 Additional Backend APIs (No Frontend UI)

### ✅ USE CASE 6: Receive Notifications (UC06)
**Actor**: Patient, Doctor
**Status**: ✅ BACKEND IMPLEMENTED

**API Endpoint**:
```bash
GET /api/notifications/user_notifications/?user_id={user_id}
```

**Notification Types**:
- Appointment Confirmations
- Appointment Reminders
- Test Results Available
- Prescription Renewals
- Health Alerts
- System Maintenance

**Project Outcome**: Automated notification system integrated in backend

---

### ✅ USE CASE 7: Manage Doctor Schedule (UC07)
**Actor**: Doctor
**Status**: ✅ BACKEND IMPLEMENTED

**API Endpoints**:
```bash
# Set Doctor Schedule
POST /api/doctors/{doctor_id}/set_schedule/
Content-Type: application/json

{
  "doctor_id": "DOC-2001",
  "working_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
  "start_time": "09:00:00",
  "end_time": "17:00:00"
}

# View Doctor Schedule
GET /api/doctors/{doctor_id}/schedule/
```

**Project Outcome**: Doctor availability management system

---

### ✅ USE CASE 8: View Appointment Schedule (UC08)
**Actor**: Doctor
**Status**: ✅ BACKEND IMPLEMENTED

**API Endpoint**:
```bash
GET /api/doctors/{doctor_id}/appointments/
```

**Project Outcome**: Doctor's appointment viewing functionality

---

### ✅ USE CASE 9: Manage Patient Records (UC09)
**Actor**: Doctor
**Status**: ✅ BACKEND IMPLEMENTED

**API Endpoints**:
```bash
# List All Patients
GET /api/patients/

# Get Patient Details
GET /api/patients/{patient_id}/
```

**Project Outcome**: Patient record access for doctors

---

### ✅ USE CASE 10: Update Medical Records (UC10)
**Actor**: Doctor
**Status**: ✅ BACKEND IMPLEMENTED

**API Endpoints**:
```bash
# Create Medical Record
POST /api/medical-records/

# Update Medical Record
PUT /api/medical-records/{record_id}/
```

**Project Outcome**: Medical record creation and update functionality

---

### ✅ USE CASE 11: Process Appointments (UC11)
**Actor**: Doctor
**Status**: ✅ BACKEND IMPLEMENTED

**API Endpoints**:
```bash
# Confirm Appointment
POST /api/appointments/{appointment_id}/confirm/

# Complete Appointment
POST /api/appointments/{appointment_id}/complete/
```

**Project Outcome**: Appointment processing workflow for doctors

---

### ✅ USE CASE 12: Generate Reports & Analytics (UC12)
**Actor**: System Admin
**Status**: ✅ BACKEND IMPLEMENTED

**API Endpoint**:
```bash
GET /api/analytics/dashboard/
```

**Response**:
```json
{
  "total_patients": 5,
  "total_doctors": 3,
  "total_appointments": 12,
  "pending_appointments": 4,
  "completed_appointments": 7,
  "system_uptime": "98.5%"
}
```

**Analytics Features**:
- Patient Demographics Report
- Doctor Utilization Report
- Appointment Statistics
- Revenue Analysis
- Recent Activity Log

**Project Outcome**: Comprehensive system analytics dashboard

---

## 🚀 How to Run the Complete Project

### Prerequisites
- Docker and Docker Compose installed
- Git installed
- Ports 8000, 3000, 5431, 6379 available

### Step 1: Start Backend
```bash
# Navigate to backend directory
cd /Users/varuntejachundru/Documents/Github/HARMS_Inclass_Activity

# Start backend services
docker-compose up -d

# Apply migrations (if needed)
docker-compose exec web python manage.py migrate

# Verify backend is running
curl http://localhost:8000/api/
```

### Step 2: Start Frontend
```bash
# Navigate to frontend directory
cd /Users/varuntejachundru/Documents/Github/HARMS_Inclass_Activity_Frontend

# Start frontend service
docker-compose up frontend-dev -d

# Verify frontend is running
curl http://localhost:3000
```

### Step 3: Access the Application
- **Frontend UI**: http://localhost:3000
- **Backend API**: http://localhost:8000/api/
- **Django Admin**: http://localhost:8000/admin/

---

## 📸 Screenshot Capture Guide

### Required Screenshots (5 Total)

1. **Use Case 1 - Login/Register**
   - URL: http://localhost:3000/login
   - Capture: Both forms with sample data

2. **Use Case 2 - Patient Dashboard**
   - URL: http://localhost:3000/dashboard
   - Capture: Full dashboard with all sections

3. **Use Case 3 - Book Appointment**
   - URL: http://localhost:3000/book-appointment
   - Capture: Form with selected specialty, doctor, date, and time slot

4. **Use Case 4 - Manage Appointments**
   - URL: http://localhost:3000/manage-appointments
   - Capture: Table showing all appointments with status badges

5. **Use Case 5 - View Medical Records**
   - URL: http://localhost:3000/medical-records
   - Capture: All three sections (Lab Results, Medications, History)

### Screenshot Best Practices
- Use browser width of at least 1200px
- Capture full page including navigation
- Ensure all sections are visible
- Use high resolution for clarity
- Show actual data in forms and tables

---

## 📋 Complete API Endpoint Reference

### Patient Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patients/register/` | Register new patient |
| GET | `/api/patients/` | List all patients |
| GET | `/api/patients/{id}/` | Get patient details |
| PUT | `/api/patients/{id}/` | Update patient |
| GET | `/api/patients/{id}/appointments/` | Get patient appointments |
| GET | `/api/patients/{id}/medical_records/` | Get patient medical records |

### Doctor Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/doctors/` | Register new doctor |
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/{id}/` | Get doctor details |
| POST | `/api/doctors/{id}/set_schedule/` | Set doctor schedule |
| GET | `/api/doctors/{id}/schedule/` | View doctor schedule |
| GET | `/api/doctors/{id}/appointments/` | Get doctor appointments |

### Appointment Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/appointments/` | Book new appointment |
| GET | `/api/appointments/` | List all appointments |
| GET | `/api/appointments/{id}/` | Get appointment details |
| POST | `/api/appointments/{id}/confirm/` | Confirm appointment |
| POST | `/api/appointments/{id}/cancel/` | Cancel appointment |

### Medical Record Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/medical-records/` | Create medical record |
| GET | `/api/medical-records/` | List all records |
| GET | `/api/medical-records/{id}/` | Get record details |
| PUT | `/api/medical-records/{id}/` | Update record |

### Other Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/time-slots/create_slots/` | Create time slots |
| GET | `/api/time-slots/available/` | Get available slots |
| GET | `/api/notifications/user_notifications/` | Get notifications |
| GET | `/api/analytics/dashboard/` | Get analytics |

---

## 🎨 Design Patterns Implemented

1. **Repository Pattern**: Data handling and database abstraction in Django models
2. **Mediator Pattern**: Handles doctor-patient interactions through appointment system
3. **CQRS**: Separate read/write operations for scalability

---

## 📦 Database Schema

### Core Models
- **User** (Base class with authentication)
- **Patient** (Extends User)
- **Doctor** (Extends User)
- **SystemAdmin** (Extends User)
- **Appointment** (Manages bookings)
- **MedicalRecord** (Stores patient health data)
- **Notification** (User alerts)
- **Schedule** (Doctor availability)
- **TimeSlot** (Available appointment times)
- **Medication** (Prescription tracking)
- **TestResult** (Lab results)
- **Analytics** (System metrics)
- **Report** (Generated reports)

---

## ✅ Testing & Validation

### Backend API Testing
- **Test Script**: `test_apis.py`
- **Demo Script**: `demo_use_cases.sh`
- **Test Coverage**: 10/12 APIs fully functional

### Frontend Testing
- All 5 implemented pages are functional
- Navigation between pages works
- Forms accept and validate input
- Tables display data correctly
- Responsive design implemented

---

## 📝 Submission Checklist

- [x] Backend repository with complete API implementation
- [x] Frontend repository with 5 key use case prototypes
- [x] Docker configuration for both frontend and backend
- [x] Database migrations and schema
- [x] README documentation in both repos
- [x] API testing scripts
- [x] GitHub repository links
- [ ] Screenshots for all 5 implemented use cases
- [x] This comprehensive submission document

---

## 👥 Project Team

**Team**: ACS 560_Project_Team_2
**Course**: ACS 560 Software Engineering
**Submission Date**: November 15, 2025

---

## 📞 Repository Links (Quick Reference)

- **Backend**: https://github.com/varunteja99/HARMS_Inclass_Activity
- **Frontend**: https://github.com/varunteja99/HARMS_Inclass_Activity_Frontend

---

**Document Version**: 1.0
**Last Updated**: November 15, 2025
**Status**: Ready for Submission ✅
