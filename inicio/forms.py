from django import forms

class FormularioVideojuegos(forms.Form):
    nombre = forms.CharField(max_length = 50)
    desarrollador = forms.CharField(max_length = 50)
    descripcion = forms.CharField(max_length = 500)
    categoria = forms.CharField(max_length = 50)
    fecha_lanzamiento = forms.IntegerField()

class FormularioBuscarVideojuego(forms.Form):
    consulta = forms.CharField(label="", max_length=50, required=False)
