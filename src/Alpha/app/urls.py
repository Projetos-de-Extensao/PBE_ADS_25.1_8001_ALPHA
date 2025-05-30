# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import MoradorViewSet


router = DefaultRouter()
router.register(r'Morador', MoradorViewSet, basename='Morador')

urlpatterns = [
    path('', include(router.urls)),
    path('Domicilio', DomicilioAPIView.as_view(), name='domicilio'),
]