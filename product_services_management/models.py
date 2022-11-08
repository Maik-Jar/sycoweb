
from django.db import models

# Create your models here.

class Impuesto(models.Model):
    nombre= models.CharField(max_length=10)
    detalle= models.CharField(max_length=60)
    porcentaje= models.DecimalField(max_digits=3, decimal_places=0)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Item(models.Model):
    impuesto= models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

class Servicio(models.Model):
    codigo= models.OneToOneField(Item, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=90)
    precio= models.DecimalField(max_digits=12, decimal_places=2)

class Categoria(models.Model):
    nombre= models.CharField(max_length=40)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo= models.OneToOneField(Item, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    categoria= models.ForeignKey(Categoria, on_delete= models.CASCADE)
    precio= models.DecimalField(max_digits=12, decimal_places=2)
    cantidad= models.IntegerField()


