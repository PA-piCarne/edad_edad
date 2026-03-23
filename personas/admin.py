from django.contrib import admin

from .models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_persona', 'apellido', 'cedula', 'edad')
    search_fields = ('apellido', 'cedula')
