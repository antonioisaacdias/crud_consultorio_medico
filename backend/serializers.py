from rest_framework import serializers
from .models import Professional

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
        
    def update(self, instance, validated_data):
        
        allowed_fiels = ['name', 'email', 'crm', 'specialty']
        
        for attr, value in validated_data.items():
            if attr not in allowed_fiels:
                raise serializers.ValidationError(f'Campo {attr} não pode ser atualizado.')
            setattr(instance, attr, value)
        instance.save()
        return instance