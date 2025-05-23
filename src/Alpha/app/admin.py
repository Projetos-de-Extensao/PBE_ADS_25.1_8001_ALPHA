from django.contrib import admin
from .models import Administrador, Domicilio, Morador

admin.site.register(Administrador)
admin.site.register(Domicilio)
admin.site.register(Morador)
