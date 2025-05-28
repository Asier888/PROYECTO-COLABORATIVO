# Definición de rutas URL para la aplicación principal.

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import RegistroUsuarioView


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('inicio/', views.index, name='index'),
    path('api/tarea/<int:pk>/', views.TareaDetalleAPI.as_view(), name='api_detalle_tarea'),
    
    path('lista_cliente', views.ListClienteView.as_view(), name='lista_cliente'),
    path('<int:pk>/detalles_cliente', views.DetailClienteView.as_view(), name='detalles_cliente'),
    path('<int:pk>/borrar_cliente', views.DeleteClienteView.as_view(), name='borrar_cliente'),
    path('crear_cliente', views.CreateClienteView.as_view(), name='crear_cliente' ),
    path('<int:pk>/modificar_cliente', views.UpdateClienteView.as_view(), name='modificar_cliente'),

    path('lista_empleado', views.ListEmpleadoView.as_view(), name='lista_empleado'),
    path('<int:pk>/detalles_empleado', views.DetailEmpleadoView.as_view(), name='detalles_empleado'),
    path('<int:pk>/borrar_empleado', views.DeleteEmpleadoView.as_view(), name='borrar_empleado'),
    path('crear_empleado', views.CreateEmpleadoView.as_view(), name='crear_empleado' ),
    path('<int:pk>/modificar_empleado', views.UpdateEmpleadoView.as_view(), name='modificar_empleado'),

    path('lista_tarea', views.ListTareaView.as_view(), name='lista_tarea'),
    path('<int:pk>/detalles_tarea', views.DetailTareaView.as_view(), name='detalles_tarea'),
    path('<int:pk>/borrar_tarea', views.DeleteTareaView.as_view(), name='borrar_tarea'),
    path('crear_tarea', views.CreateTareaView.as_view(), name='crear_tarea' ),
    path('<int:pk>/modificar_tarea', views.UpdateTareaView.as_view(), name='modificar_tarea'),

    path('lista_proyecto', views.ListProyectoView.as_view(), name='lista_proyecto'),
    path('<int:pk>/detalles_proyecto', views.DetailProyectoView.as_view(), name='detalles_proyecto'),
    path('<int:pk>/borrar_proyecto', views.DeleteProyectoView.as_view(), name='borrar_proyecto'),
    path('crear_proyecto', views.CreateProyectoView.as_view(), name='crear_proyecto' ),
    path('<int:pk>/modificar_proyecto', views.UpdateProyectoView.as_view(), name='modificar_proyecto'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
]