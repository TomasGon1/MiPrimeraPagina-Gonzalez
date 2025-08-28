from django.shortcuts import render, redirect
from inicio.models import Videojuegos
from inicio.forms import FormularioVideojuegos, FormularioBuscarVideojuego
from django.db.models import Q
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

def inicio(request):
    
    return render(request, 'inicio.html')

def cargar_juego(request):
    
    print(request.POST)

    if request.method == "POST":
        formulario = FormularioVideojuegos(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            juego = Videojuegos(nombre=data.get('nombre'), desarrollador=data.get('desarrollador'), descripcion=data.get('descripcion'), categoria=data.get('categoria'), fecha_lanzamiento=data.get('fecha_lanzamiento'))
            juego.save()

            return redirect('listado_de_juegos')
    else:
        formulario = FormularioVideojuegos()
        
    return render(request, 'cargar_juego.html', {'formulario': formulario})

def listado_de_juegos(request):
    
    formulario = FormularioBuscarVideojuego(request.GET)
    if formulario.is_valid():
        consulta = formulario.cleaned_data['consulta']
        if consulta:
            juegos_buscados = Videojuegos.objects.filter(
                Q(nombre__icontains=consulta) |
                Q(desarrollador__icontains=consulta) |
                Q(categoria__icontains=consulta)
            )
        else:
            juegos_buscados = Videojuegos.objects.all()
    else:
        juegos_buscados = Videojuegos.objects.all()
   
    return render(request, 'listado_de_juegos.html', {"juegos": juegos_buscados, "formulario": formulario})

def detalle_juego(request, id_juego):
    
    juego = Videojuegos.objects.get(id=id_juego)
    
    return render(request, 'detalle_juego.html', {'juego': juego} )

class BorrarJuego(DeleteView):
    model = Videojuegos
    template_name = "borrar_juego.html"
    success_url = reverse_lazy('listado_de_juegos')

class ActualizarJuego(UpdateView):
    model = Videojuegos
    template_name = "actualizar_juego.html"
    success_url = reverse_lazy('listado_de_juegos')
    fields = '__all__'
