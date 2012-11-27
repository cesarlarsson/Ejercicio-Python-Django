from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return  self.nombre
    

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio_venta = models.FloatField()
    precio_compra = models.FloatField()
    categoria = models.ForeignKey(Categoria)
    
    def __str__(self):
        return  self.nombre