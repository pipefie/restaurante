# Create your models here.
from django.db import models

class TipoMasa(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Pizza(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    tipo_masa = models.ForeignKey(TipoMasa, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    primera_vez = models.BooleanField()
    numero_comensales = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora}"
