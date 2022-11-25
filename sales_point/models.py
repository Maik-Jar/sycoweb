from django.db import models
from customers_management.models import Cliente
from product_services_management.models import Item
# Create your models here.

class Cotizacion(models.Model):

    agnio= models.DateField(auto_now_add=True, verbose_name='Año')
    numero= models.IntegerField(editable=False)
    cliente= models.ForeignKey(Cliente, on_delete= models.CASCADE, null=True, blank=True)
    fecha_hora= models.DateTimeField(auto_now_add= True, verbose_name='Fecha / Hora')
    subtotal= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    descuento= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    total= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    estado= models.BooleanField(default=True)
    creacion= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Cotizacion No. '+str(self.agnio.year)+'-'+str(self.numero)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['agnio', 'numero'], name='unique_cotizacion'), ]

class DetalleCotizacion(models.Model):

    id_cotizacion= models.ForeignKey(Cotizacion, on_delete= models.CASCADE)
    item= models.ForeignKey(Item, on_delete= models.CASCADE)
    descuento_item= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    cantidad_item= models.IntegerField(default=1)

class DetalleItem(models.Model):

    id_detalle_cotizacion= models.ForeignKey(DetalleCotizacion, on_delete= models.CASCADE)
    detalle= models.CharField(max_length=150, null= True, blank= True, default='')
