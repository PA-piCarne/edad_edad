from django.db import models


class Persona(models.Model):
    numero_persona = models.PositiveIntegerField(unique=True)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    edad = models.PositiveIntegerField()

    class Meta:
        ordering = ['numero_persona']

    def __str__(self):
        return f'Persona {self.numero_persona} - {self.apellido}'
