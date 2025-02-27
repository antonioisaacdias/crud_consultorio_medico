from django.db import models
from uuid import uuid4

class Professional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    crm = models.CharField(max_length=10 ,unique=True, null=False, blank=False)
    specialty = models.CharField(max_length=80, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=11, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    appointment_datetime = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    