from django.contrib import admin
from .models import Domicilio, Morador, CaracteristicasDomicilio


admin.site.register(Domicilio)
admin.site.register(Morador)
admin.site.register(CaracteristicasDomicilio)