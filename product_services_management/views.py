from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormCrearImpuesto, FormModificarImpuesto, FormCrearCategoria, FormModificarCategoria
from django.core.paginator import Paginator
from .models import Impuesto, Categoria
import json
# Create your views here.


def gestion_impuestos(request):

    if request.method == 'GET':

        impuestos= Paginator(Impuesto.objects.all(), 5)

        if request.GET.get('page'):

            page_number= request.GET.get('page')

            impuesto_page= impuestos.get_page(page_number)
        
            return render(request, 'gestion_impuestos.html',
            {'impuestos': impuesto_page,
            'form':FormModificarImpuesto}
            )

        else:

            impuesto_page= impuestos.get_page(1)
        
            return render(request, 'gestion_impuestos.html',
            {'impuestos': impuesto_page,
            'form':FormModificarImpuesto}
            )

    else:

        data_json_string = str(request.POST.get('json'))

        json_file = json.loads(data_json_string)

        if json_file['codigo'] == 1:

            data = json.dumps(Impuesto.objects.get(id=json_file['impuestoid']))

            return JsonResponse({'data': data})

def crear_impuesto(request):

    if request.method == 'GET':
        
        return render(request, 'formulario_crear_impuesto.html', {'form': FormCrearImpuesto})

    else:

        formimpuesto = FormModificarImpuesto(request.POST)

        if formimpuesto.is_valid():
            impuesto= formimpuesto.save(commit= False)
            impuesto.estado= True
            impuesto.save()
            return redirect('gestion impuestos')

            # return render(request, 'formulario_impuesto.html', 
            # {'form': formimpuesto,
            # 'success':'El impuesto ha sido creado.'}
            # )

        else:
            return render(request, 'formulario_crear_impuesto.html',
            {'form': formimpuesto,
            'error':'Formulario invalido, no se ha podico crear el impuesto.'}
            )

def modificar_impuesto(request, idimpuesto):

    if request.method == 'GET':

        impuesto= get_object_or_404(Impuesto, pk= idimpuesto)

        formimpuesto = FormModificarImpuesto(instance= impuesto)

        return render(request, 'formulario_modificar_impuesto.html',
        {'form': formimpuesto}
        )
    
    else:
        
        impuesto= get_object_or_404(Impuesto, pk= idimpuesto)

        formimpuesto = FormModificarImpuesto(request.POST, instance= impuesto)

        if formimpuesto.is_valid():
            formimpuesto.save()
            return render(request, 'formulario_modificar_impuesto.html',
            {'form': formimpuesto,
            'success':'El impuesto ha sido modificado.'}
            )
        else:
            return render(request, 'formulario_modificar_impuesto.html',
            {'form': formimpuesto,
            'error':'Formulario invalido, no se ha podico modificar el impuesto.'}
            )

def gestion_categorias(request):

    if request.method == 'GET':

        categoria= Paginator(Categoria.objects.all(), 5)

        if request.GET.get('page'):

            page_number= request.GET.get('page')

            categoria_page= categoria.get_page(page_number)
        
            return render(request, 'gestion_categorias.html',
                            {'categorias': categoria_page,
                             'form': FormCrearCategoria}
                        )

        else:

            categoria_page= categoria.get_page(1)
        
            return render(request, 'gestion_categorias.html',
                            {'categorias': categoria_page,
                             'form': FormCrearCategoria}
                        )

def crear_categoria(request):
    
    if request.method == 'GET':

        return render(request, 'formulario_crear_categoria.html', {'form':FormCrearCategoria} )

    else:

        formcategoria = FormCrearCategoria(request.POST)

        if formcategoria.is_valid():
            impuesto= formcategoria.save(commit= False)
            impuesto.estado= True
            impuesto.save()
            return redirect('gestion categorias')

            # return render(request, 'formulario_impuesto.html', 
            # {'form': formimpuesto,
            # 'success':'El impuesto ha sido creado.'}
            # )

        else:
            return render(request, 'formulario_crear_categoria.html',
            {'form': formcategoria,
            'error':'Formulario invalido, no se ha podico crear la categoria.'}
            )

def modificar_categoria(request, idcategoria):

    if request.method == 'GET':

        categoria= get_object_or_404(Categoria, pk= idcategoria)

        formcategoria = FormModificarCategoria(instance= categoria)

        return render(request, 'formulario_modificar_categoria.html',
        {'form': formcategoria}
        )
    
    else:
        
        categoria= get_object_or_404(Categoria, pk= idcategoria)

        formcategoria = FormModificarCategoria(request.POST, instance= categoria)

        if formcategoria.is_valid():
            formcategoria.save()
            return render(request, 'formulario_modificar_categoria.html',
            {'form': formcategoria,
            'success':'La Categoria ha sido modificada.'}
            )
        else:
            return render(request, 'formulario_modificar_categoria.html',
            {'form': formcategoria,
            'error':'Formulario invalido, no se ha podico modificar la categoria.'}
            )