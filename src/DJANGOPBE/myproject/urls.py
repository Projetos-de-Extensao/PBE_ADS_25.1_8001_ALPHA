# myproject/urls.py
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from django.contrib import admin
schema_view = get_schema_view(
   openapi.Info(
      title="API de Produtos",
      default_version='v1',
      description="API para gerenciamento de produtos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@empresa.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # ... URLs existentes
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]