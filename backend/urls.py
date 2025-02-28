from django.urls import path
from . import views

urlpatterns = [
    path('professionals/', views.professionals, name='professionals'),
    path('professionals/<uuid:pk>/', views.professionals_detail, name='professionals_detail'),
    path('professionals/<uuid:professional_pk>/appointments/', views.professional_appointments, name='professionals_appointments'),
    path('patients/', views.patients, name='patients'),
    path('patients/<uuid:pk>/', views.patients_detail, name='patient_detail'),
    path('patients/<uuid:patient_pk>/appointments/', views.patient_appointments, name='patient_appointments'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/<uuid:pk>/', views.appointments_detail, name='appointments_detail'),
    path('appointments/<str:date>/', views.appointments_by_date, name='appointments_by_date'),
]