from django import forms


class FormularioBuscarEspecialidad(forms.Form):
    nombre = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }))