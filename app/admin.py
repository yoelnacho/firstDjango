from django.contrib import admin
#importamos nuestro modelo
from app.models import Datos

#registramos nuestro modelo creado en el sitio
admin.site.register(Datos)