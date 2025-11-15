#!/usr/bin/env python
"""
Script to test HARMS APIs and demonstrate use cases
"""
import requests
import json
from datetime import datetime, timedelta
import random

BASE_URL = "http://localhost:8000/api"

def print_response(title, response):
    """Print formatted response"""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    else:
        print(f"Error: {response.text}")
    print(f"{'='*60}\n")

def use_case_1_patient_registration():
    """Use Case 1: Patient Registration"""
    print("\n" + "🏥 USE CASE 1: Patient Registration ".center(60, "="))

    patient_data = {
        "patient_id": f"PAT-{random.randint(1000, 9999)}",
        "full_name": "John Doe",
        "email": f"john.doe{random.randint(1, 999)}@example.com",
        "phone_number": "+1-555-0123",
        "date_of_birth": "1990-05-15",
        "insurance_info": "Blue Cross Blue Shield - Policy #12345",
        "emergency_contact": "Jane Doe: +1-555-0124",
        "address": "123 Main St, Boston, MA 02101"
    }

    response = requests.post(f"{BASE_URL}/patients/register/", json=patient_data)
    print_response("✅ Patient Registration", response)
    return response.json() if response.status_code == 201 else None

def use_case_2_doctor_registration():
    """Use Case 2: Doctor Registration and Schedule Setup"""
    print("\n" + "👨‍⚕️ USE CASE 2: Doctor Registration & Schedule ".center(60, "="))

    doctor_data = {
        "doctor_id": f"DOC-{random.randint(1000, 9999)}",
        "full_name": "Dr. Sarah Johnson",
        "email": f"dr.johnson{random.randint(1, 999)}@hospital.com",
        "phone_number": "+1-555-0125",
        "specialty": "Cardiology",
        "license_number": f"MD-{random.randint(100000, 999999)}",
        "department": "Cardiology Department"
    }

    response = requests.post(f"{BASE_URL}/doctors/", json=doctor_data)
    print_response("✅ Doctor Registration", response)

    if response.status_code == 201:
        doctor = response.json()
        doctor_id = doctor['doctor_id']

        # Set doctor's schedule
        schedule_data = {
            "doctor_id": doctor_id,
            "working_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "start_time": "09:00:00",
            "end_time": "17:00:00"
        }

        schedule_response = requests.post(
            f"{BASE_URL}/doctors/{doctor_id}/set_schedule/",
            json=schedule_data
        )
        print_response("✅ Doctor Schedule Created", schedule_response)
        return doctor
    return None

def use_case_3_create_time_slots():
    """Use Case 3: Create Available Time Slots"""
    print("\n" + "⏰ USE CASE 3: Create Time Slots ".center(60, "="))

    today = datetime.now()
    slots_data = {
        "start_date": today.strftime("%Y-%m-%d"),
        "end_date": (today + timedelta(days=7)).strftime("%Y-%m-%d"),
        "start_time": "09:00",
        "end_time": "17:00"
    }

    response = requests.post(f"{BASE_URL}/time-slots/create_slots/", json=slots_data)
    print_response("✅ Time Slots Created", response)
    return response.json() if response.status_code == 201 else None

def use_case_4_book_appointment(patient_id, doctor_id, slot_id):
    """Use Case 4: Book an Appointment"""
    print("\n" + "📅 USE CASE 4: Book Appointment ".center(60, "="))

    appointment_data = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "appointment_date": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"),
        "time_slot_id": slot_id,
        "specialty": "Cardiology",
        "reason_for_visit": "Annual checkup and heart health consultation",
        "notes": "Patient has family history of heart disease"
    }

    response = requests.post(f"{BASE_URL}/appointments/", json=appointment_data)
    print_response("✅ Appointment Booked", response)
    return response.json() if response.status_code == 201 else None

def use_case_5_view_appointments(patient_id):
    """Use Case 5: View Patient Appointments"""
    print("\n" + "📋 USE CASE 5: View Patient Appointments ".center(60, "="))

    response = requests.get(f"{BASE_URL}/patients/{patient_id}/appointments/")
    print_response("✅ Patient Appointments", response)

def use_case_6_create_medical_record(patient_id, doctor_id):
    """Use Case 6: Create Medical Record"""
    print("\n" + "📄 USE CASE 6: Create Medical Record ".center(60, "="))

    record_data = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "visit_date": datetime.now().strftime("%Y-%m-%d"),
        "diagnosis": "Hypertension Stage 1",
        "treatment_plan": "Lifestyle modifications, regular monitoring, medication if needed",
        "visit_type": "Follow-up"
    }

    response = requests.post(f"{BASE_URL}/medical-records/", json=record_data)
    print_response("✅ Medical Record Created", response)
    return response.json() if response.status_code == 201 else None

def use_case_7_view_medical_records(patient_id):
    """Use Case 7: View Medical Records"""
    print("\n" + "📚 USE CASE 7: View Medical Records ".center(60, "="))

    response = requests.get(f"{BASE_URL}/patients/{patient_id}/medical_records/")
    print_response("✅ Patient Medical Records", response)

def use_case_8_notifications(patient_id):
    """Use Case 8: View Notifications"""
    print("\n" + "🔔 USE CASE 8: Patient Notifications ".center(60, "="))

    response = requests.get(f"{BASE_URL}/notifications/user_notifications/?user_id={patient_id}")
    print_response("✅ Patient Notifications", response)

def use_case_9_analytics():
    """Use Case 9: System Analytics Dashboard"""
    print("\n" + "📊 USE CASE 9: System Analytics ".center(60, "="))

    response = requests.get(f"{BASE_URL}/analytics/dashboard/")
    print_response("✅ System Analytics Dashboard", response)

def use_case_10_appointment_management(appointment_id):
    """Use Case 10: Appointment Management (Confirm/Cancel)"""
    print("\n" + "✅ USE CASE 10: Appointment Management ".center(60, "="))

    # Confirm appointment
    response = requests.post(f"{BASE_URL}/appointments/{appointment_id}/confirm/")
    print_response("✅ Appointment Confirmed", response)

def main():
    """Run all use case tests"""
    print("\n" + "🏥 HARMS - Healthcare Appointment and Record Management System ".center(80, "="))
    print("API Testing and Use Case Demonstration".center(80))
    print("=" * 80)

    # Use Case 1: Register Patient
    patient = use_case_1_patient_registration()
    if not patient:
        print("❌ Failed to register patient. Exiting...")
        return

    patient_id = patient['data']['patient_id']

    # Use Case 2: Register Doctor
    doctor = use_case_2_doctor_registration()
    if not doctor:
        print("❌ Failed to register doctor. Exiting...")
        return

    doctor_id = doctor['doctor_id']

    # Use Case 3: Create Time Slots
    slots_result = use_case_3_create_time_slots()
    if not slots_result:
        print("❌ Failed to create time slots. Exiting...")
        return

    slot_id = slots_result['slot_ids'][0]

    # Use Case 4: Book Appointment
    appointment = use_case_4_book_appointment(patient_id, doctor_id, slot_id)
    if not appointment:
        print("❌ Failed to book appointment. Exiting...")
        return

    appointment_id = appointment['data']['appointment_id']

    # Use Case 5: View Patient Appointments
    use_case_5_view_appointments(patient_id)

    # Use Case 6: Create Medical Record
    medical_record = use_case_6_create_medical_record(patient_id, doctor_id)

    # Use Case 7: View Medical Records
    use_case_7_view_medical_records(patient_id)

    # Use Case 8: View Notifications
    use_case_8_notifications(patient_id)

    # Use Case 9: System Analytics
    use_case_9_analytics()

    # Use Case 10: Appointment Management
    use_case_10_appointment_management(appointment_id)

    print("\n" + "✅ All Use Cases Completed Successfully! ".center(80, "="))
    print("\nSummary:".center(80))
    print(f"Patient ID: {patient_id}")
    print(f"Doctor ID: {doctor_id}")
    print(f"Appointment ID: {appointment_id}")
    print("\nYou can now capture screenshots for your submission!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
