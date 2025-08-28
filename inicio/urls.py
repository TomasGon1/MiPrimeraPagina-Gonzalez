from django.urls import path
from inicio.views import inicio, cargar_juego, listado_de_juegos, detalle_juego, BorrarJuego, ActualizarJuego

urlpatterns = [
    path('', inicio, name='inicio'),
    path('juegos/', listado_de_juegos, name='listado_de_juegos'),
    path('juegos/cargar/', cargar_juego, name='cargar_juego'),
    path('juegos/<int:id_juego>/', detalle_juego, name='detalle_juego'),
    path('juegos/<int:pk>/borrar', BorrarJuego.as_view(), name='borrar_juego'),
    path('juegos/<int:pk>/actualizar', ActualizarJuego.as_view(), name='actualizar_juego'),
]
