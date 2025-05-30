from django.urls import path
from . import views
from .views import AdministradorViewSet, DomicilioViewSet, MoradorViewSet

router = DefaultRouter()
router.register(r'administrador', AdministradorViewSet)
router.register(r'domicilio', DomicilioViewSet)
router.register(r'morador', MoradorViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', views.index, name='index'),
]
