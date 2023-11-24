from django.urls import path
from .views import *

urlpatterns = [
    path('', ver_especialidades, name='ver_especialidades'),
    path('buscar/', buscar_especialidades, name='buscar_especialidades'),
    path('especialidad/<int:pk>', VerEspecialidadView.as_view(), name='ver_especialidad'),
    path('nuevo/', NuevaEspecialidadView.as_view(), name='crear_especialidad'),
    path('especialidad/<int:pk>/editar/', EditarEspecialidadView.as_view(), name='editar_especialidad'),
    path('especialidad/<int:pk>/eliminar/', EliminarEspecialidadView.as_view(), name='borrar_especialidad'),
]