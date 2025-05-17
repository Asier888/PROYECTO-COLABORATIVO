from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.conf import settings
from .models import Cliente, Empleado, Tarea, Proyecto
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .forms import EmpleadoFormulario, ClienteFormulario, ProyectoFormulario, TareaFormulario

def index(request):
    return render(request, 'index.html')

class ListClienteView(ListView):
    model = Cliente
    queryset = Cliente.objects.all()

class DetailClienteView(DetailView):
    model = Cliente

class CreateClienteView(CreateView):
    model = Cliente
    form_class = ClienteFormulario
    template_name = 'cliente_formulario.html'
    success_url = reverse_lazy('cliente')

class DeleteClienteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente')

class UpdateClienteView(UpdateView):
    model = Cliente
    form_class = ClienteFormulario
    template_name = 'cliente_formulario.html'
    success_url = reverse_lazy('cliente')



class ListEmpleadoView(ListView):
    model = Empleado
    queryset = Empleado.objects.all()

class DetailEmpleadoView(DetailView):
    model = Empleado

class CreateEmpleadoView(CreateView):
    model = Empleado
    form_class = EmpleadoFormulario
    template_name = 'empleado_formulario.html'
    success_url = reverse_lazy('empleados')

class DeleteEmpleadoView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

class UpdateEmpleadoView(UpdateView):
    model = Empleado
    form_class = EmpleadoFormulario
    template_name = 'empleado_formulario.html'
    success_url = reverse_lazy('empleados')



class ListTareaView(ListView):
    model = Tarea
    queryset = Tarea.objects.all()

class DetailTareaView(DetailView):
    model = Tarea

class CreateTareaView(CreateView):
    model = Tarea
    form_class = TareaFormulario
    template_name = 'tarea_formulario.html'
    success_url = reverse_lazy('tarea')

class DeleteTareaView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('tarea')

class UpdateTareaView(UpdateView):
    model = Tarea
    form_class = TareaFormulario
    template_name = 'tarea_formulario.html'
    success_url = reverse_lazy('tarea')




class ListProyectoView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.all()

class DetailProyectoView(DetailView):
    model = Proyecto

class CreateProyectoView(CreateView):
    model = Proyecto
    form_class = ProyectoFormulario
    template_name = 'proyecto_formulario.html'
    success_url = reverse_lazy('proyecto')

class DeleteProyectoView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyecto')

class UpdateProyectoView(UpdateView):
    model = Proyecto
    form_class = ProyectoFormulario
    template_name = 'proyecto_formulario.html'
    success_url = reverse_lazy('proyecto')

