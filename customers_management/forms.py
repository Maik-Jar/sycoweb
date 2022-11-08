from django import forms
from .models import Cliente, Empresa, Persona, TipoDocumento

class FormCrearCliente(forms.ModelForm):

    class Meta:
        model= Cliente
        fields= ['tipo',]
        widgets= {'tipo': forms.Select(attrs={'class':'form-select'}, choices= [(0, 'Persona'), (1, 'Empresa')])
                }

class FormModificarCliente(forms.ModelForm):

    class Meta:
        model= Cliente
        fields= ['tipo', 'estado']
        widgets= {'tipo': forms.Select(attrs={'class':'form-select'}, choices= [(0, 'Persona'), (1, 'Empresa')]), 
                  'estado': forms.Select(attrs={'class':'form-select'}, choices=[(False, 'Inactivo'), (True, 'Activo')]),
                }

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

class FormEmpresa(forms.ModelForm):

    class Meta:
        model= Empresa
        fields= ['razon_social', 'rnc', 'telefono', 'direccion', 'email',]
        widgets= {'razon_social': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduca el nombre o razón social completo de la empresa.'}),
                  'rnc': forms.NumberInput(attrs={'class':'forms-control', 'placeholder':'Introduca el RNC de la empresa.'}),
                  'telefono': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduca el número de télefono sin guiones, ej: 8090004594'}),
                  'dirección': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduzca la dirección de residencia.'}),
                  'email': forms.EmailInput(attrs={'class':'forms-control'})
        }

class FormPersona(forms.ModelForm):

    class Meta:
        model= Persona
        fields= ['nombre', 'apellido1',  'apellido2', 'tipodocumento', 'iddocumento', 'telefono', 'direccion', 'email',]
        widgets= {'nombre': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduca el nombre completo.'}),
                  'apellido1': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduca el apellido parteno.'}),
                  'apellido2': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduca el apellido materno.'}),
                  'tipodocumento': forms.Select(attrs={'class':'form-select'}),
                  'iddocumento': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduca el número de documento sin guiones.'}),
                  'telefono': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduca el número de télefono sin guiones, ej: 8090004594'}),
                  'dirección': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Introduzca la dirección de residencia.'}),
                  'email': forms.EmailInput(attrs={'class':'forms-control'})
        }