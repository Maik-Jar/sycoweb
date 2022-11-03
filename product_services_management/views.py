from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormCrearImpuesto, FormCrearItem, FormCrearServicio, FormModificarImpuesto, FormCrearCategoria, FormModificarCategoria, FormModificarItem
from django.core.paginator import Paginator
from .models import Impuesto, Categoria, Item, Servicio
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def gestion_impuestos(request):

    if request.method == 'GET':

        impuestos= Paginator(Impuesto.objects.all().order_by('id'), 5)

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

@login_required
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

@login_required
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
    
@login_required
def eliminar_impuesto(request, idimpuesto):

    impuesto= get_object_or_404(Impuesto, pk= idimpuesto)

    if request.method == 'POST':
        impuesto.delete()
        return redirect('gestion impuestos')

@login_required
def gestion_categorias(request):

    if request.method == 'GET':

        categoria= Paginator(Categoria.objects.all().order_by('id'), 5)

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

@login_required
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

@login_required
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

@login_required
def eliminar_categoria(request, idcategoria):

    categoria= get_object_or_404(Categoria, pk= idcategoria)

    if request.method == 'POST':
        categoria.delete()
        return redirect('gestion categorias')

@login_required
def gestion_servicios(request):

    if request.method == 'GET':

        servicio= Paginator(Servicio.objects.all().order_by('codigo'), 5)

        if request.GET.get('page'):

            page_number= request.GET.get('page')

            servicio_page= servicio.get_page(page_number)
        
            return render(request, 'gestion_servicios.html',
                            {'servicios': servicio_page,
                             'form': FormCrearCategoria}
                        )

        else:

            servicio_page= servicio.get_page(1)
        
            return render(request, 'gestion_servicios.html',
                            {'servicios': servicio_page,
                             'form': FormCrearCategoria}
                        )

@login_required
def crear_servicio(request):
    
    if request.method == 'GET':

        return render(request, 'formulario_crear_servicio.html', 
        {'formservicio':FormCrearServicio,
         'formitem':FormCrearItem
        } )

    else:

        formitem = FormCrearItem(request.POST)

        if formitem.is_valid():
            item= formitem.save(commit= False)
            item.estado= True
            item.save()

            servicio= Servicio(codigo= item, descripcion= request.POST['descripcion'], precio= request.POST['precio'])
            servicio.save()
            
            return redirect('gestion servicios')

@login_required
def modificar_servicio(request, iditem):

    if request.method == 'GET':

        item= get_object_or_404(Item, pk= iditem)

        servicio= Servicio.objects.get(codigo= item)

        formmodificaritem= FormModificarItem(instance= item)

        formservicio= FormCrearServicio(instance= servicio)

        return render(request, 'formulario_modificar_servicio.html',
        {'formitem': formmodificaritem,
         'formservicio': formservicio}
        )
    
    else:
        
        item= get_object_or_404(Item, pk= iditem)

        formmodificaritem= FormModificarItem(request.POST, instance= item)

        if formmodificaritem.is_valid():

            servicio= Servicio.objects.get(codigo= item)

            formservicio= FormCrearServicio(request.POST, instance= servicio)

            if formservicio.is_valid():
                formmodificaritem.save()
                formservicio.save()

                return render(request, 'formulario_modificar_servicio.html',
                {'formitem': formmodificaritem,
                 'formservicio': formservicio,
                 'success':'El servicio ha sido modificado.'
                }
                )

            else:
                return render(request, 'formulario_modificar_servicio.html',
                {'formitem': formmodificaritem,
                 'formservicio': formservicio,
                 'error':'Formulario invalido, no se ha podido modificar el servicio.'
                }
                )

        else:
            return render(request, 'formulario_modificar_servicio.html',
                {'formitem': formmodificaritem,
                 'formservicio': formservicio,
                 'error':'Formulario invalido, no se ha podido modificar el servicio.'
                }
                )

@login_required
def eliminar_servicio(request, iditem):

    item= get_object_or_404(Item, pk= iditem)

    if request.method == 'POST':
        item.delete()
        return redirect('gestion servicios')
