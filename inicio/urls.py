from django.urls import path
from inicio.views import inicio, cargar_juego, listado_de_juegos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('juego/', listado_de_juegos, name='listado_de_juegos'),
    path('cargar/juego/', cargar_juego, name='cargar_juego')
]
