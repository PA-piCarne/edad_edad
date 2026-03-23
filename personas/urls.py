from django.urls import path

from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('personas/nueva/', views.crear_persona, name='crear_persona'),
    path('personas/', views.listar_personas, name='listar_personas'),
    path('personas/promedio-edades/', views.promedio_edades, name='promedio_edades'),
    path('personas/menor-edad/', views.persona_menor_edad, name='persona_menor_edad'),
    path('explicaciones/base-datos/', views.explicacion_base_datos, name='explicacion_base_datos'),
    path('explicaciones/lambda/', views.explicacion_lambda, name='explicacion_lambda'),
]
