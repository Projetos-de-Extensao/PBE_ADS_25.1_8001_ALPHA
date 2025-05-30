# minhaapp/api.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models import Domicilio
from app.serializers import DomicilioSerializer
from app.models import Morador
from app.serializers import MoradorSerializer


class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        Domicilios = Domicilio.objects.filter(disponivel=True)
        serializer = self.get_serializer(Domicilios, many=True)
        return Response(serializer.data)
    
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        Moradores = Morador.objects.filter(disponivel=True)
        serializer = self.get_serializer(Moradores, many=True)
        return Response(serializer.data)
    
