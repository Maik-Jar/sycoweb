from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class TipoDocumento(models.Model):
    nombre= models.CharField(max_length= 15)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class TipoCliente(models.Model): # En desuso, marcado para ser eliminado en futuras versiones. Por ahora solo esta presente pero no tiene funcionalidad ni relacion con los demas modelos.
    nombre= models.CharField(max_length= 20)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):

    TIPO_CLIENTE_CHOICES= [(1, 'Empresa'),
                           (2, 'Persona'),
                        ]

    tipo= models.IntegerField(choices= TIPO_CLIENTE_CHOICES, default=2)
    #tipo= models.ForeignKey(TipoCliente, on_delete= models.CASCADE, default=2) marcado para ser eliminada cuando se elimine el modelo TipoCliente.
    iddocumento= models.CharField(max_length=12)
    tipo_documento= models.ForeignKey(TipoDocumento, on_delete= models.CASCADE, default=1)
    razon_social= models.CharField(max_length=100, unique= True, null= True)
    nombre= models.CharField(max_length=25, null= True)
    apellido1= models.CharField(max_length= 15, null= True)
    apellido2= models.CharField(max_length= 15, null= True, blank= True)
    telefono= models.CharField(max_length=15, null= True, blank= True)
    direccion= models.CharField(max_length=100, null= True, blank= True)
    email= models.EmailField(max_length=30, null= True, blank= True)
    estado= models.BooleanField(default=True)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.tipo == 1: # Empresa
            return self.razon_social
        else: # Persona
            return self.nombre+' '+self.apellido1+' '+self.apellido2

    class Meta:
        constraints = [UniqueConstraint(fields=['iddocumento', 'tipo_documento'], name='unique_document'),]