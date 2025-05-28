# Configuración del panel de administración para registrar los modelos:
# Cliente, Empleado, Proyecto y Tarea en el admin de Django.

from django.contrib import admin
from .models import Cliente, Empleado, Proyecto, Tarea

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Proyecto)
admin.site.register(Tarea)
