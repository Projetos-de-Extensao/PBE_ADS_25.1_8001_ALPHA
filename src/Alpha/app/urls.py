# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import MoradorViewSet, DomicilioViewSet


router = DefaultRouter()
router.register(r'Morador', MoradorViewSet, basename='Morador')
router.register(r'Domicilio', DomicilioViewSet, basename= 'Domicilio')

urlpatterns = router.urls