from django import forms
from.models import Cliente, Empleado, Tarea, Proyecto

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoFormulario(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class TareaFormulario(forms.ModelForm):
    duracion = forms.IntegerField(label='Duración (días)', required=False, min_value=0)
    
    class Meta:
        model = Tarea
        fields = '__all__'

class ProyectoFormulario(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'