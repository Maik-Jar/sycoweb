from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

class customUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model= User
        fields= UserCreationForm.Meta.fields
        widget= {'username': TextInput(attrs={'class':'form-control'}),
                 'password1': PasswordInput(attrs={'class':'form-control'}),
                 'password2': PasswordInput(attrs={'class':'form-control'})
                 }
