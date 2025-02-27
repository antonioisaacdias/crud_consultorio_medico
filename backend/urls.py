from django.urls import path
from . import views

urlpatterns = [
    path('professionals/', views.professionals, name='professionals'),
    path('professionals/<uuid:pk>/', views.professionals_detail, name='professionals_detail'),
    path('patients/', views.patients, name='patients'),
    path('patients/<uuid:pk>/', views.patients_detail, name='patient_detail')
]