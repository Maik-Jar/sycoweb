from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormImpuesto
from .models import Impuesto
# Create your views here.

def homepage(request):

    if request.method == 'GET':
        form= FormImpuesto()
        return render(request, 'formulario_impuesto.html', {'form':form})
    else:
        print(request.POST)
        return HttpResponse(request.POST)

def gestion_impuestos(request):

    if request.method == 'GET':
        impuestos= Impuesto.objects.all()
        return render(request, 'tabla_impuestos.html', {'impuestos':impuestos})
    else:
        print(request.POST)
        return HttpResponse(request.POST)
    