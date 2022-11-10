from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    nombre= models.CharField(max_length= 15)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class TipoCliente(models.Model):
    nombre= models.CharField(max_length= 20)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    tipo= models.ForeignKey(TipoCliente, on_delete= models.CASCADE)
    iddocumento= models.CharField(max_length=12, unique= True)
    tipo_documento= models.ForeignKey(TipoDocumento, on_delete= models.CASCADE)
    razon_social= models.CharField(max_length=100, unique= True, null= True)
    nombre= models.CharField(max_length=25, null= True)
    apellido1= models.CharField(max_length= 15, null= True)
    apellido2= models.CharField(max_length= 15, null= True)
    telefono= models.CharField(max_length=12, null= True)
    direccion= models.CharField(max_length=60, null= True)
    email= models.EmailField(max_length=30, null= True)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)
