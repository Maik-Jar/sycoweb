
from django import forms
from .models import Impuesto, Servicio, Categoria, Producto

class FormCrearImpuesto(forms.ModelForm): 
    class Meta:
        model= Impuesto
        fields= ['nombre', 'detalle', 'porcentaje'] 
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre común del impuesto.'}),
                  'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre detallado del impuesto.'}),
                  'porcentaje': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Introduzca el porcentaje del impuesto, ej: para 18% = 18'}),
        }

class FormModificarImpuesto(forms.ModelForm): 
    class Meta:
        model= Impuesto
        fields= ['nombre', 'detalle', 'porcentaje', 'estado'] 
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre común del impuesto.'}),
                  'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre detallado del impuesto.'}),
                  'porcentaje': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Introduzca el porcentaje del impuesto, ej: para 18% = 18'}),
                  'estado': forms.Select(attrs={'class':'form-select'}, choices=[(False, 'Inactivo'), (True, 'Activo')]),
        }

class FormServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['codigo', 'descripcion', 'precio']

class FormCrearCategoria(forms.ModelForm):
    class Meta:
        model= Categoria
        fields= ['nombre']
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre de la categoria.'}),
                  }

class FormModificarCategoria(forms.ModelForm):
    class Meta:
        model= Categoria
        fields= ['nombre', 'estado']
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre de la categoria.'}),
                  'estado':forms.Select(attrs={'class':'form-select'}, choices=[(False, 'Inactivo'), (True, 'Activo')]),
        }

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'cantidad']