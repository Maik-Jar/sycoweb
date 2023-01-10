from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def homepage(request):

    if request.method == 'GET':
        return render(request, 'base.html')

    if request.method == 'POST':
        return HttpResponse(request.POST)

def signin(request):

    if request.method == 'GET':
        return render(request, 'login.html', {'form':AuthenticationForm})

    if request.method == 'POST': 
        user= authenticate(request, username= request.POST['username'], password= request.POST['password'])
        
        if user is None:
            
            return render(request, 'login.html', {
                'form':AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecto.'
            })
        
        if user is not None:

            login(request, user)
            return redirect('homepage')

@login_required
def signout(request):

    logout(request)
    return redirect('signin')
