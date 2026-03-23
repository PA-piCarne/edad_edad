from django import forms

from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['numero_persona', 'apellido', 'cedula', 'edad']
        labels = {
            'numero_persona': 'Número de persona',
            'apellido': 'Apellido',
            'cedula': 'Cédula',
            'edad': 'Edad',
        }
