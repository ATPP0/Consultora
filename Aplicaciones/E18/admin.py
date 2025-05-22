from django.contrib import admin

from Aplicaciones.E18.models import Empleado, EmpresaAgricola, Proyecto

# Register your models here.
admin.site.register(EmpresaAgricola)
admin.site.register(Empleado)
admin.site.register(Proyecto)
