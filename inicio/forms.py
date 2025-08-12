from django import forms

class FormularioVideojuegos(forms.Form):
    nombre = forms.CharField(max_length=20)
    desarrollador = forms.CharField(max_length=20)
    categoria = forms.CharField(max_length=20)
    fecha_lanzamiento = forms.IntegerField()