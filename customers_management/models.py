from django.db import models

# Create your models here.

class Cliente(models.Model):
    tipo= models.BinaryField(default= 0) # 0= Persona, 1= Empresa
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):

        if self.tipo == 0:
            return 'Persona'
        else:
            return 'Empresa'

class Empresa(models.Model):
    codigo= models.OneToOneField(Cliente, on_delete= models.CASCADE)
    rnc= models.BigIntegerField(unique= True)
    razon_social= models.CharField(max_length=100, unique= True)
    telefono= models.CharField(max_length=12)
    direccion= models.CharField(max_length=60, null= True)
    email= models.EmailField(max_length=30, null= True)

class TipoDocumento(models.Model):
    nombre= models.CharField(max_length= 15)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    codigo= models.OneToOneField(Cliente, on_delete= models.CASCADE)
    iddocumento= models.CharField(max_length=12, unique= True)
    tipo_documento= models.ForeignKey(TipoDocumento, on_delete= models.CASCADE)
    nombre= models.CharField(max_length=25, unique= True)
    apellido1= models.CharField(max_length= 15)
    apellido2= models.CharField(max_length= 15, null= True)
    telefono= models.CharField(max_length=12, null= True)
    direccion= models.CharField(max_length=60, null= True)
    email= models.EmailField(max_length=30, null= True)