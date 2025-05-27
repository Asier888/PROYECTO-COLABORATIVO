from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


from .models import Cliente, Empleado, Tarea, Proyecto
from .forms import EmpleadoFormulario, ClienteFormulario, ProyectoFormulario, TareaFormulario

def index(request):
    return render(request, 'index.html')

class RegistroUsuarioView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = '/'

class ListClienteView(LoginRequiredMixin, ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    login_url = '/login/'

class DetailClienteView(LoginRequiredMixin, DetailView):
    model = Cliente
    context_object_name = 'lista_cliente'
    login_url = '/login/'

class CreateClienteView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteFormulario
    template_name = 'cliente_formulario.html'
    success_url = reverse_lazy('lista_cliente')
    login_url = '/login/'

class DeleteClienteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('lista_cliente')
    login_url = '/login/'

class UpdateClienteView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteFormulario
    template_name = 'cliente_formulario.html'
    success_url = reverse_lazy('lista_cliente')
    login_url = '/login/'

class ListEmpleadoView(LoginRequiredMixin, ListView):
    model = Empleado
    queryset = Empleado.objects.all()
    login_url = '/login/'

class DetailEmpleadoView(LoginRequiredMixin, DetailView):
    model = Empleado
    context_object_name = 'lista_empleado'
    login_url = '/login/'

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = self.object.tareas.all()
        return context

class CreateEmpleadoView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoFormulario
    template_name = 'empleado_formulario.html'
    success_url = reverse_lazy('lista_empleado')
    login_url = '/login/'

class DeleteEmpleadoView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'appEmpresaDjango/empleado_delete.html'
    success_url = reverse_lazy('lista_empleado')
    login_url = '/login/'

class UpdateEmpleadoView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoFormulario
    template_name = 'empleado_formulario.html'
    success_url = reverse_lazy('lista_empleado')
    login_url = '/login/'

class ListTareaView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea_list.html'
    login_url = '/login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.GET.get('estado')
        prioridad = self.request.GET.get('prioridad')

        if estado:
            queryset = queryset.filter(estado=estado)
        if prioridad:
            queryset = queryset.filter(prioridad=prioridad)

        return queryset

class DetailTareaView(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'lista_tarea'
    login_url = '/login/'

class CreateTareaView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaFormulario
    template_name = 'tarea_formulario.html'
    success_url = reverse_lazy('lista_tarea')
    login_url = '/login/'

class DeleteTareaView(LoginRequiredMixin, DeleteView):
    model = Tarea
    success_url = reverse_lazy('lista_tarea')
    login_url = '/login/'

class UpdateTareaView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaFormulario
    template_name = 'tarea_formulario.html'
    success_url = reverse_lazy('lista_tarea')
    login_url = '/login/'

class ListProyectoView(LoginRequiredMixin, ListView):
    model = Proyecto
    queryset = Proyecto.objects.all()
    login_url = '/login/'

class DetailProyectoView(LoginRequiredMixin, DetailView):
    model = Proyecto
    context_object_name = 'lista_proyecto'
    login_url = '/login/'

class CreateProyectoView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoFormulario
    template_name = 'proyecto_formulario.html'
    success_url = reverse_lazy('lista_proyecto')
    login_url = '/login/'

class DeleteProyectoView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    success_url = reverse_lazy('lista_proyecto')
    login_url = '/login/'

class UpdateProyectoView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoFormulario
    template_name = 'proyecto_formulario.html'
    success_url = reverse_lazy('lista_proyecto')
    login_url = '/login/'


class TareaDetalleAPI(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            tarea = Tarea.objects.get(pk=pk)
            data = {
                'descripcion': tarea.descripcion,
                'fecha_inicio': tarea.fecha_inicio.strftime('%Y-%m-%d'),
                'fecha_fin': tarea.fecha_fin.strftime('%Y-%m-%d'),
                'prioridad': tarea.prioridad,
                'estado': tarea.estado,
            }
            return JsonResponse(data)
        except Tarea.DoesNotExist:
            return JsonResponse({'error': 'Tarea no encontrada'}, status=404)