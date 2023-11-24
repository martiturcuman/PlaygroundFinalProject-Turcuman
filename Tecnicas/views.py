from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *
from .forms import *


def ver_especialidades(request):
    especialidades = Especialidad.objects.all().order_by('id')
    return render(request, 'Tecnicas/ver_especialidades.html', { 'especialidades' : especialidades })


def buscar_especialidades(request):
    nombre = request.GET.get('nombre', None)

    if nombre:
        especialidades = Especialidad.objects.filter(nombre__icontains=nombre)
    else:
        especialidades = Especialidad.objects.all()

    especialidades = especialidades.order_by('id')

    formulario_buscar_especialidades = FormularioBuscarEspecialidad()

    return render(request, 'Tecnicas/buscar_especialidades.html', { 'formulario_buscar_especialidades' : formulario_buscar_especialidades, 'especialidades' : especialidades })


class VerEspecialidadView(DetailView):
    model = Especialidad
    template_name = 'Tecnicas/ver_especialidad.html'


class NuevaEspecialidadView(LoginRequiredMixin, CreateView):
    model = Especialidad
    template_name = 'Tecnicas/crear_especialidad.html'
    success_url = '/especialidades/'
    fields = ['nombre', 'abreviatura', 'tecnicas', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EditarEspecialidadView(LoginRequiredMixin, UpdateView):
    model = Especialidad
    template_name = 'Tecnicas/editar_especialidad.html'
    success_url = '/especialidades/'
    fields = ['nombre', 'abreviatura', 'tecnicas', 'imagen']


class EliminarEspecialidadView(LoginRequiredMixin, DeleteView):
    model = Especialidad
    template_name = 'Tecnicas/borrar_especialidad.html'
    success_url = '/especialidades/'