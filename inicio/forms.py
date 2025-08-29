from django import forms
from inicio.models import Videojuegos

class FormularioVideojuegos(forms.Form):
    nombre = forms.CharField(max_length = 50)
    desarrollador = forms.CharField(max_length = 50)
    descripcion = forms.CharField(max_length = 500)
    categoria = forms.CharField(max_length = 50)
    fecha_lanzamiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    imagen = forms.ImageField(required = False)

class FormularioBuscarVideojuego(forms.Form):
    consulta = forms.CharField(label="", max_length=50, required=False)

class VideojuegoActualizar(forms.ModelForm):
    class Meta():
        model = Videojuegos
        fields = '__all__'  
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'}),
        }
