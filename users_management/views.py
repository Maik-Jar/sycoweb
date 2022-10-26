from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import customUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.

def userpage(request):

    if request.method == 'GET':

        return render(request, 'user.html', {'form':UserCreationForm})

    else:

        if request.POST['password1'] == request.POST['password2']:
            
                user= User.objects.create_user(username= request.POST['username'], password= request.POST['password1'])
                print(user.password)
                user.save()
                login(request, user)
            
                return HttpResponse('usuario creado!!')

        return  HttpResponse('contrasena no coinciden!')

def user_login(request):

    if request.method == 'GET':

        return render(request, 'login.html')

    else:
        # try:
        user= User.objects.get(username= request.POST['username'])
        print(user.password)
        if user.password == request.POST['password']:

            login(request, user)

            return redirect('homepage')

        else:

            return JsonResponse({'mensaje':'la contrasena es incorrecta'})
        # except:

        #     return JsonResponse({'mensaje':'el usuario no existe'})