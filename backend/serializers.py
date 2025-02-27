from rest_framework import serializers
from .models import Professional, Patient, Appointment

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
        
    def update(self, instance, validated_data):
        allowed_fields = ['name', 'email', 'crm', 'specialty']
        
        for attr, value in validated_data.items():
            if attr not in allowed_fields:
                raise serializers.ValidationError(f'Campo {attr} não pode ser atualizado.')
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    
    def update(self, instance, validated_data):
        allowed_fields = ['name', 'email', 'address', 'phone', 'cpf', 'birth_date']
        
        for attr, value in validated_data.items():
            if attr not in allowed_fields:
                raise serializers.ValidationError(f'Campo {attr} não pode ser atualizado.')
            setattr(instance, attr, value)
        instance.save()
        return instance

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
    def update(self, instance, validated_data):
        allowed_fields = ['appointment_datetime']

        for attr, value in validated_data.items():
            if attr not in allowed_fields:
                raise serializers.ValidationError(f'Campo {attr} não pode ser atualizado.')
            setattr(instance, attr, value)
        instance.save()
        return instance