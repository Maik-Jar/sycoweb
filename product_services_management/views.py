from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormCrearImpuesto, FormModificarImpuesto
from .models import Impuesto
import json
# Create your views here.


def gestion_impuestos(request):

    if request.method == 'GET':
        impuestos = Impuesto.objects.all()
        
        return render(request, 'tabla_impuestos.html', {'impuestos': impuestos})

    else:

        data_json_string = str(request.POST.get('json'))

        json_file = json.loads(data_json_string)

        if json_file['codigo'] == 1:

            data = json.dumps(Impuesto.objects.get(id=json_file['impuestoid']))

            return JsonResponse({'data': data})


def crear_impuesto(request):

    if request.method == 'GET':
        
        return render(request, 'formulario_impuesto.html', {'form': FormCrearImpuesto})

    else:

        data_json_string = str(request.POST.get('json'))

        json_file = json.loads(data_json_string)

        if json_file['codigo'] == 1:

            pass

def modificar_impuesto(request, idimpuesto):

    if request.method == 'GET':

        impuesto= get_object_or_404(Impuesto, pk= idimpuesto)

        formimpuesto = FormModificarImpuesto(instance= impuesto)

        return render(request, 'formulario_impuesto.html', {'form': formimpuesto})
    
    else:
        
        impuesto= get_object_or_404(Impuesto, pk= idimpuesto)

        formimpuesto = FormModificarImpuesto(request.POST, instance= impuesto)

        if formimpuesto.is_valid():
            formimpuesto.save()
            return redirect('gestion impuestos')
        else:
            return render(request, 'formulario_impuesto.html', {'form': formimpuesto, 'error':'Formulario invalido'})
