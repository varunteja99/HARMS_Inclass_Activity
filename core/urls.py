from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet, DoctorViewSet, AppointmentViewSet,
    MedicalRecordViewSet, TimeSlotViewSet, NotificationViewSet,
    ReportViewSet, AnalyticsViewSet
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'medical-records', MedicalRecordViewSet, basename='medicalrecord')
router.register(r'time-slots', TimeSlotViewSet, basename='timeslot')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'analytics', AnalyticsViewSet, basename='analytics')

urlpatterns = [
    path('api/', include(router.urls)),
]
