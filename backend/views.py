from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Professional, Patient, Appointment
from .serializers import ProfessionalSerializer

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
            return Response({'message' : 'Cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
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
            updated_professional = serializer.update(professional, serializer.validated_data)
            return Response({'message': 'Informações atualizadas com sucesso!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)