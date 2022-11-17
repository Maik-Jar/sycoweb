from django import forms
from .models import Cliente, TipoDocumento, TipoCliente

class FormCrearTipoDocumento(forms.ModelForm):

    class Meta:
        model= TipoDocumento
        fields= ['nombre',]
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre del tipo de documento.'})}

class FormModificarTipoDocumento(forms.ModelForm):

    class Meta:
        model= TipoDocumento
        fields= ['nombre','estado',]
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre del tipo de documento.'}),
                  'estado': forms.Select(attrs={'class':'form-select'}, choices=[(False, 'Inactivo'), (True, 'Activo')]),
                    
                }

class FormCrearTipoCliente(forms.ModelForm):

    class Meta:
        model= TipoCliente
        fields= ['nombre']
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre del tipo de cliente.'})
        }

class FormModificarTipoCliente(forms.ModelForm):

    class Meta:
        model= TipoCliente
        fields= ['nombre','estado',]
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre del tipo de cliente.'}),
                  'estado': forms.Select(attrs={'class':'form-select'}, choices=[(False, 'Inactivo'), (True, 'Activo')]),
                    
                }

class FormCliente(forms.ModelForm):

    class Meta:
        model= Cliente
        fields= ['tipo', 'iddocumento', 'tipo_documento', 'razon_social', 'nombre', 'apellido1', 'apellido2', 'telefono', 'direccion', 'email']
        widgets= {'tipo': forms.Select(attrs={'class':'form-select'}),
                  'tipo_documento':forms.Select(attrs={'class':'form-select'}),
                  'iddocumento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba número de documento sin guiones.'}),
                  'razon_social': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre (razón social) de la empresa.'}),
                  'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre completo.'}),
                  'apellido1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el apellido paterno.'}),
                  'apellido2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el apellido materno.'}),
                  'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el número de telefono sin guiones'}),
                  'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba la dirección'}),
                  'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escriba el email'}),
                }
        labels= {'tipo':'Tipo de Cliente', 'iddocumento':'No. Documento', 'tipo_documento':'Tipo Documento', 'apellido1':'1er. Apellido', 'apellido2':'2do. Apellido', 'razon_social':'Razón Social', 'telefono':'Teléfono', 'direccion':'Dirección'}

# class FormCliente(forms.ModelForm):

#     class Meta:
#         model= Cliente
#         fields= ['tipo', 'iddocumento', 'tipo_documento']
#         widgets= {'tipo': forms.Select(attrs={'class':'form-select'}),
#                   'tipo_documento':forms.Select(attrs={'class':'form-select'}),
#                   'iddocumento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba número de documento sin guiones.'}),
#                 }
#         labels= {'tipo':'Tipo de Cliente', 'iddocumento':'No. Documento', 'tipo_documento':'Tipo Documento'}

class FormCrearClienteEmpresa(forms.ModelForm):

    class Meta:
        model= Cliente
        fields= ['tipo', 'iddocumento', 'tipo_documento', 'razon_social', 'telefono', 'direccion', 'email']
        widgets= {'razon_social': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre (razón social) de la empresa.'}),
                  'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el número de telefono sin guiones'}),
                  'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba la dirección'}),
                  'email': forms.EmailInput(attrs={'required': False, 'class':'form-control', 'placeholder':'Escriba el email'}),
                }
        labels= {'razon_social':'Razón Social'}

class FormCrearClientePersona(forms.ModelForm):

    class Meta:
        model= Cliente
        fields= ['tipo', 'iddocumento', 'tipo_documento', 'nombre', 'apellido1', 'apellido2', 'telefono', 'direccion', 'email']
        widgets= {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el nombre completo.'}),
                  'apellido1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el apellido paterno.'}),
                  'apellido2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el apellido materno.'}),
                  'telefono': forms.TextInput(attrs={'required': False, 'class':'form-control', 'placeholder':'Escriba el número de telefono sin guiones'}),
                  'direccion': forms.TextInput(attrs={'required': False, 'class':'form-control', 'placeholder':'Escriba la dirección'}),
                  'email': forms.EmailInput(attrs={'required': False, 'class':'form-control', 'placeholder':'Escriba el email'}),
                }   
        labels= {'apellido1':'1er. Apellido', 'apellido2':'2do. Apellido'}