from django.db import models

class Videojuegos(models.Model):
    nombre = models.CharField(max_length=20)
    desarrollador = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    fecha_lanzamiento = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.desarrollador} {self.categoria} {self. fecha_lanzamiento}'
