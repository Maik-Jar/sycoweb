from django import forms
from .models import Cotizacion

#

class FormCrearCotizacion(forms.ModelForm):

    class Meta:
        model= Cotizacion
        fields= ['']