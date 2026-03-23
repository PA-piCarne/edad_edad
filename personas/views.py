from django.shortcuts import redirect, render

from .forms import PersonaForm
from .models import Persona


promedio_lambda = lambda edades: (sum(edades) / len(edades)) if edades else 0
persona_menor_lambda = lambda personas: min(personas, key=lambda persona: persona.edad) if personas else None
serializar_persona_lambda = lambda persona: {
    'id': persona.id,
    'numero_persona': persona.numero_persona,
    'apellido': persona.apellido,
    'cedula': persona.cedula,
    'edad': persona.edad,
}


def lobby(request):
    return render(request, 'personas/lobby.html')


def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/crear_persona.html', {'form': form})


def listar_personas(request):
    personas = Persona.objects.all()
    personas_serializadas = list(map(serializar_persona_lambda, personas))
    return render(request, 'personas/listar_personas.html', {'personas': personas_serializadas})


def promedio_edades(request):
    edades = list(map(lambda persona: persona.edad, Persona.objects.all()))
    promedio = promedio_lambda(edades)
    return render(request, 'personas/promedio_edades.html', {'promedio': promedio, 'total_personas': len(edades)})


def persona_menor_edad(request):
    personas = list(Persona.objects.all())
    persona = persona_menor_lambda(personas)
    return render(request, 'personas/persona_menor_edad.html', {'persona': persona})


def explicacion_base_datos(request):
    pasos = [
        'Django usa la configuración DATABASES de config/settings.py para decidir a qué motor conectarse.',
        'Se seleccionó sqlite3 porque crea un archivo local llamado db.sqlite3 en la raíz del proyecto.',
        'Ese archivo puede abrirse directamente con DB Browser for SQLite para revisar tablas y registros.',
        'Cuando ejecutes migrate, Django creará las tablas internas y la tabla personas_persona.',
        'Cada vez que guardes una persona desde el formulario, Django insertará una fila nueva en SQLite.',
    ]
    return render(request, 'personas/explicacion_base_datos.html', {'pasos': pasos})


def explicacion_lambda(request):
    ejemplos = [
        {
            'titulo': 'Promedio de edades',
            'codigo': 'promedio_lambda = lambda edades: (sum(edades) / len(edades)) if edades else 0',
            'descripcion': 'Recibe una lista de edades y devuelve el promedio. Si no hay datos, devuelve 0.',
        },
        {
            'titulo': 'Persona con menor edad',
            'codigo': 'persona_menor_lambda = lambda personas: min(personas, key=lambda persona: persona.edad) if personas else None',
            'descripcion': 'Busca la persona cuya edad sea la más pequeña usando una lambda interna como criterio.',
        },
        {
            'titulo': 'Serialización para la tabla',
            'codigo': "serializar_persona_lambda = lambda persona: {'id': persona.id, 'numero_persona': persona.numero_persona, 'apellido': persona.apellido, 'cedula': persona.cedula, 'edad': persona.edad}",
            'descripcion': 'Transforma cada objeto Persona en un diccionario fácil de renderizar en la plantilla.',
        },
    ]
    return render(request, 'personas/explicacion_lambda.html', {'ejemplos': ejemplos})
