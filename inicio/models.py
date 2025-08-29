from django.db import models

class Videojuegos(models.Model):
    nombre = models.CharField(max_length = 50)
    desarrollador = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 500, default="Sin Descripcion")
    categoria = models.CharField(max_length = 50)
    fecha_lanzamiento = models.DateField(null = True, blank = True)
    imagen = models.ImageField(upload_to = "imagenes_juegos", null = True, blank = True)
    
    def __str__(self):
        return f'{self.nombre} {self.desarrollador} {self.descripcion} {self.categoria} {self.fecha_lanzamiento}'
