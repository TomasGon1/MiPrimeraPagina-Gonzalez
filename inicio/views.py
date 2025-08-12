from django.shortcuts import render, redirect
from inicio.models import Videojuegos
from inicio.forms import FormularioVideojuegos

def inicio(request):
    
    return render(request, 'inicio.html')

def cargar_juego(request):
    
    print(request.POST)

    if request.method == "POST":
        formulario = FormularioVideojuegos(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            juego = Videojuegos(nombre=data.get('nombre'), desarrollador=data.get('desarrollador'), categoria=data.get('categoria'), fecha_lanzamiento=data.get('fecha_lanzamiento'))
            juego.save()

            return redirect('listado_de_juegos')
    else:
        formulario = FormularioVideojuegos()
        
    return render(request, 'cargar_juego.html', {'formulario': formulario})

def listado_de_juegos(request):
    
    juegos = Videojuegos.objects.all()
    
    return render(request, 'listado_de_juegos.html', {"juegos": juegos})