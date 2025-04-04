from django.db import models
from .plato import Plato
from .mesero import Mesero
from .mesa import Mesa
from .cliente import Cliente

class Orden(models.Model):
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    ]
    #relaciones
    platos = models.ManyToManyField(Plato, related_name='ordenes')
    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE, related_name='ordenes')
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='ordenes')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierto')
    fecha_hora = models.DateTimeField()

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Orden {self.id} - Mesa {self.mesa.numero} ({self.estado})"
