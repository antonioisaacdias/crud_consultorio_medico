from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Professional, Patient, Appointment
from .serializers import ProfessionalSerializer, PatientSerializer, AppointmentSerializer
from datetime import datetime

@api_view(['GET', 'POST'])
def professionals(request):
    if request.method == 'GET':
        professionals = Professional.objects.all()
        serializer = ProfessionalSerializer(professionals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfessionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Médico cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def professionals_detail(request, pk):
    if request.method == 'GET':
        professional = Professional.objects.get(id=pk)
        serializer = ProfessionalSerializer(professional)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        professional = Professional.objects.get(id=pk)
        professional.delete()
        return Response({'message': 'Excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
        professional = Professional.objects.get(id=pk)
        serializer = ProfessionalSerializer(professional, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.update(professional, serializer.validated_data)
            return Response({'message': 'Informações atualizadas com sucesso!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Paciente cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH','DELETE'])
def patients_detail(request, pk):
    if request.method == 'GET':
        patient = Patient.objects.get(id=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        patient = Patient.objects.get(id=pk)
        patient.delete()
        return Response({'message': 'Excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        patient = Patient.objects.get(id=pk)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.update(patient, serializer.validated_data)
            return Response({'message': 'Informações atualizadas com sucesso!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def appointments(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Consulta agendada com sucesso!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def appointments_detail(request, pk):
    if request.method == 'GET':
        appointment = Appointment.objects.get(id=pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        appointment = Appointment.objects.get(id=pk)
        appointment.delete()
        return Response({'message': 'Excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PATCH':
        appointment = Appointment.objects.get(id=pk)
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.update(appointment, serializer.validated_data)
            return Response({'message': 'Informações atualizadas com sucesso!'}, status=status.HTTP_200_OK)
        

@api_view(['GET'])
def professional_appointments(request, professional_pk):
    appointments = Appointment.objects.filter(professional_id=professional_pk)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def patient_appointments(request, patient_pk):
    appointments = Appointment.objects.filter(patient_id=patient_pk)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appointments_by_date(request, date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({"error": "Formato de data inválido. Use AAAA-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
    appointments = Appointment.objects.filter(appointment_datetime__date=date_obj)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)
    