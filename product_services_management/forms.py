
from django.forms import ModelForm
from .models import Impuesto, Servicio, Categoria, Producto

class FormImpuesto(ModelForm): 
    class Meta:
        model = Impuesto
        fields = ['nombre', 'detalle', 'porcentaje']

class FormServicio(ModelForm):
    class Meta:
        model = Servicio
        fields = ['codigo', 'descripcion', 'precio']

class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']

class FormProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'cantidad']