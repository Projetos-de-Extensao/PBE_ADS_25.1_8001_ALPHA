from rest_framework import serializers
from app.models import Morador
from app.models import Domicilio

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'

# Serializer para o formulario aceitar formato dd/mm/aaaa
class DataSerializer(serializers.ModelSerializer):
    Morador.data_nascimento = serializers.DateField(input_formats=['%d/%m/%Y'])