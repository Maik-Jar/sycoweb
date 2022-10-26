from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import FormImpuesto
from .models import Impuesto
import json
# Create your views here.


def gestion_impuestos(request):

    if request.method == 'GET':
        impuestos = Impuesto.objects.all()
        form = FormImpuesto()
        return render(request, 'tabla_impuestos.html', {'impuestos': impuestos, 'form': form})

    else:

        data_json_string = str(request.POST.get('json'))

        json_file = json.loads(data_json_string)

        if json_file['codigo'] == 1:

            data = json.dumps(Impuesto.objects.get(id=json_file['impuestoid']))

            return JsonResponse({'data': data})


def form_impuesto(request):

    if request.method == 'GET':
        form = FormImpuesto()
        return render(request, 'formulario_impuesto.html', {'form': form})

    else:

        data_json_string = str(request.POST.get('json'))

        json_file = json.loads(data_json_string)

        if json_file['codigo'] == 1:

            form = FormImpuesto(instance=Impuesto.objects.get(
                id=json_file['impuestoid']))
            return HttpResponse({'form': form})
