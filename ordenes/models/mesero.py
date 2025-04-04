from django.db import models


class Mesero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100,default="ApellidoDesconocido")
    telefono = models.CharField(max_length=20, default="Desconocido")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
