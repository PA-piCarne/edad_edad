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
