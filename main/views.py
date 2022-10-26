from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def homepage(request):

    if request.method == 'GET':

        return render(request, 'base.html')
    else:
        print(request.POST)
        return HttpResponse(request.POST)

def signin(request):

    if request.method == 'GET':
    
        return render(request, 'login.html', {'form':AuthenticationForm})

    else:
        
        user= authenticate(request, username= request.POST['username'], password= request.POST['password'])
        
        print(user)
        if user is None:

            return render(request, 'login.html', {
                'form':AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:

            login(request, user)

            return redirect('homepage')

def signout(request):

    logout(request)
    return redirect('signin')
