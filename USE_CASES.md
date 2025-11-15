# HARMS - Healthcare Appointment and Record Management System

## Implemented Use Cases and API Endpoints

### Use Case 1: Patient Registration
**Endpoint:** `POST /api/patients/register/`

**Description:** Register a new patient in the system

**Request Body:**
```json
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

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/patients/register/ \
  -H "Content-Type: application/json" \
  -d '{"patient_id": "PAT-1001", "full_name": "John Doe", "email": "john.doe@example.com", "phone_number": "+1-555-0123", "date_of_birth": "1990-05-15", "insurance_info": "Blue Cross - #12345", "emergency_contact": "Jane Doe: +1-555-0124", "address": "123 Main St, Boston, MA"}'
```

---

### Use Case 2: Doctor Registration
**Endpoint:** `POST /api/doctors/`

**Description:** Register a new doctor in the system

**Request Body:**
```json
{
  "doctor_id": "DOC-2001",
  "full_name": "Dr. Sarah Johnson",
  "email": "dr.johnson@hospital.com",
  "phone_number": "+1-555-0125",
  "specialty": "Cardiology",
  "license_number": "MD-123456",
  "department": "Cardiology Department"
}
```

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -d '{"doctor_id": "DOC-2001", "full_name": "Dr. Sarah Johnson", "email": "dr.johnson@hospital.com", "phone_number": "+1-555-0125", "specialty": "Cardiology", "license_number": "MD-123456", "department": "Cardiology Department"}'
```

---

### Use Case 3: Set Doctor Schedule
**Endpoint:** `POST /api/doctors/{doctor_id}/set_schedule/`

**Description:** Set availability schedule for a doctor

**Request Body:**
```json
{
  "working_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
  "start_time": "09:00:00",
  "end_time": "17:00:00"
}
```

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/doctors/DOC-2001/set_schedule/ \
  -H "Content-Type: application/json" \
  -d '{"working_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "start_time": "09:00:00", "end_time": "17:00:00"}'
```

---

### Use Case 4: Create Time Slots
**Endpoint:** `POST /api/time-slots/create_slots/`

**Description:** Create available time slots for appointments

**Request Body:**
```json
{
  "start_date": "2025-11-14",
  "end_date": "2025-11-21",
  "start_time": "09:00",
  "end_time": "17:00"
}
```

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/time-slots/create_slots/ \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2025-11-14", "end_date": "2025-11-21", "start_time": "09:00", "end_time": "17:00"}'
```

---

### Use Case 5: Book Appointment
**Endpoint:** `POST /api/appointments/`

**Description:** Book a new appointment for a patient

**Request Body:**
```json
{
  "patient_id": "PAT-1001",
  "doctor_id": "DOC-2001",
  "appointment_date": "2025-11-16 10:00:00",
  "time_slot_id": "TS-12345678",
  "specialty": "Cardiology",
  "reason_for_visit": "Annual checkup and heart health consultation",
  "notes": "Patient has family history of heart disease"
}
```

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/appointments/ \
  -H "Content-Type: application/json" \
  -d '{"patient_id": "PAT-1001", "doctor_id": "DOC-2001", "appointment_date": "2025-11-16 10:00:00", "time_slot_id": "TS-12345678", "specialty": "Cardiology", "reason_for_visit": "Annual checkup", "notes": "Family history of heart disease"}'
```

---

### Use Case 6: View Patient Appointments
**Endpoint:** `GET /api/patients/{patient_id}/appointments/`

**Description:** Retrieve all appointments for a specific patient

**Example Command:**
```bash
curl -X GET http://localhost:8000/api/patients/PAT-1001/appointments/
```

---

### Use Case 7: Confirm Appointment
**Endpoint:** `POST /api/appointments/{appointment_id}/confirm/`

**Description:** Confirm a pending appointment

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/appointments/APT-12345678/confirm/
```

---

### Use Case 8: Cancel Appointment
**Endpoint:** `POST /api/appointments/{appointment_id}/cancel/`

**Description:** Cancel an existing appointment

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/appointments/APT-12345678/cancel/
```

---

### Use Case 9: Create Medical Record
**Endpoint:** `POST /api/medical-records/`

**Description:** Create a new medical record for a patient visit

**Request Body:**
```json
{
  "patient_id": "PAT-1001",
  "doctor_id": "DOC-2001",
  "visit_date": "2025-11-14",
  "diagnosis": "Hypertension Stage 1",
  "treatment_plan": "Lifestyle modifications, regular monitoring",
  "visit_type": "Follow-up"
}
```

**Example Command:**
```bash
curl -X POST http://localhost:8000/api/medical-records/ \
  -H "Content-Type: application/json" \
  -d '{"patient_id": "PAT-1001", "doctor_id": "DOC-2001", "visit_date": "2025-11-14", "diagnosis": "Hypertension Stage 1", "treatment_plan": "Lifestyle modifications", "visit_type": "Follow-up"}'
```

---

### Use Case 10: View Medical Records
**Endpoint:** `GET /api/patients/{patient_id}/medical_records/`

**Description:** Retrieve all medical records for a patient

**Example Command:**
```bash
curl -X GET http://localhost:8000/api/patients/PAT-1001/medical_records/
```

---

### Use Case 11: View Notifications
**Endpoint:** `GET /api/notifications/user_notifications/?user_id={user_id}`

**Description:** Retrieve all notifications for a user

**Example Command:**
```bash
curl -X GET "http://localhost:8000/api/notifications/user_notifications/?user_id=PAT-1001"
```

---

### Use Case 12: System Analytics Dashboard
**Endpoint:** `GET /api/analytics/dashboard/`

**Description:** Get system-wide analytics and statistics

**Example Command:**
```bash
curl -X GET http://localhost:8000/api/analytics/dashboard/
```

**Response:**
```json
{
  "total_patients": 5,
  "total_doctors": 3,
  "total_appointments": 12,
  "pending_appointments": 4,
  "completed_appointments": 7
}
```

---

## Additional Available Endpoints

### List All Patients
```bash
curl -X GET http://localhost:8000/api/patients/
```

### List All Doctors
```bash
curl -X GET http://localhost:8000/api/doctors/
```

### List All Appointments
```bash
curl -X GET http://localhost:8000/api/appointments/
```

### View Available Time Slots
```bash
curl -X GET http://localhost:8000/api/time-slots/available/
```

### View Doctor Schedule
```bash
curl -X GET http://localhost:8000/api/doctors/DOC-2001/schedule/
```

### View Doctor Appointments
```bash
curl -X GET http://localhost:8000/api/doctors/DOC-2001/appointments/
```

---

## Running the Project

1. Start the Docker containers:
```bash
docker-compose up -d
```

2. Access the API:
- API Root: http://localhost:8000/api/
- Django Admin: http://localhost:8000/admin/

3. Run the demo script:
```bash
chmod +x demo_use_cases.sh
./demo_use_cases.sh
```

---

## Technology Stack

- **Backend Framework:** Django 5.2.7
- **REST API:** Django REST Framework 3.16.1
- **Database:** PostgreSQL 15
- **Caching:** Redis 7
- **Containerization:** Docker & Docker Compose
- **Programming Language:** Python 3.11

---

## Project Structure

```
HARMS_Inclass_Activity/
├── config/                 # Django project configuration
│   ├── settings.py        # Main settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── core/                  # Main application
│   ├── models.py         # Database models
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   ├── urls.py           # App URLs
│   └── enums.py          # Enumerations
├── docker-compose.yml     # Docker services
├── Dockerfile            # Container definition
├── requirements.txt      # Python dependencies
└── manage.py            # Django management
```

---

## Screenshots for Submission

### Recommended Screenshots:
1. Patient Registration Response
2. Doctor Registration Response
3. Appointment Booking Response
4. Patient Appointments List
5. Medical Records Creation
6. Notifications List
7. Analytics Dashboard
8. Doctor Schedule
9. Time Slots Creation
10. Appointment Confirmation

Use the demo script or curl commands above to generate API responses for screenshots.
