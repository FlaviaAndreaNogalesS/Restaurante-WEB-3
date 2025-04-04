from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre
