from django import forms
from .models import Cotizacion, DetalleCotizacion, DetalleItem
from customers_management.models import TipoDocumento
#

class FormCrearCotizacion(forms.Form):

    TIPO_DOCUMENTO_CHOICES = list(TipoDocumento.objects.filter(estado= True).values_list('id', 'nombre'))

    id_cliente = forms.IntegerField(widget= forms.HiddenInput)
    nombre_cliente = forms.CharField(max_length= 60, label= 'Cliente', widget=forms.TextInput(attrs={'class':'form-control'}))
    tipo_documento = forms.IntegerField(label='Tipo Documento', widget= forms.Select(attrs={'class':'form-select', 'style':'width:100%;'}, choices=TIPO_DOCUMENTO_CHOICES))
    documento_cliente = forms.CharField(max_length= 60, label= 'No. Documento', widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono_cliente = forms.CharField(max_length= 60, label= 'Teléfono', widget=forms.TextInput(attrs={'class':'form-control','readonly':True}))


class FormCrearDetalleCotizacion(forms.ModelForm):

    class Meta:
        model= DetalleCotizacion
        fields= ['item','cantidad_item']
        widgets= {'item':forms.NumberInput(attrs={'class':'form-control', 'onlyread':True}),
                  'cantidad_item':forms.NumberInput(attrs={'class':'form-control', 'onlyread':True}),
        
        }
