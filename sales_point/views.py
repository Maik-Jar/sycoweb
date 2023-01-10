from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from django.db import transaction
from .models import Cotizacion, DetalleCotizacion
from .forms import FormCrearCotizacion, FormCrearDetalleCotizacion
from sequences import Sequence
import json

# Create your views here.

@login_required
def gestion_cotizaciones(request):

    if request.method == 'GET':
        
        cotizacion= Paginator(Cotizacion.objects.all().order_by('agnio', 'numero'), 9)

        if request.GET.get('page'):

            page_number= request.GET.get('page')

            cotizacion_page= cotizacion.get_page(page_number)
        
            return render(request, 'gestion_cotizaciones.html',
            {'cotizaciones': cotizacion_page,
            'form':'FormModificarTipoDocumento'}
            )

        else:

            cotizacion_page= cotizacion.get_page(1)
        
            return render(request, 'gestion_cotizaciones.html',
            {'cotizaciones': cotizacion_page,
            'form':'FormModificarTipoDocumento'}
            )

@login_required
def crear_cotizacion(request):

    if request.method == 'GET':

        return render(request, 'formulario_crear_cotizacion.html', {'form':FormCrearCotizacion})

    else:

        datos_cotizacion =  json.loads(request.body)

        encabezado= datos_cotizacion['encabezado']
        detalle= datos_cotizacion['detalle']

        if encabezado['id_cliente'] == '':
            encabezado['id_cliente'] = None
        elif encabezado['nombre_cliente'] == '':
            encabezado['nombre_cliente'] = None

        # Create sequence object
        numero_cotizacion = Sequence('cotizacion')

        try:
            with transaction.atomic():
                nueva_cotizacion = Cotizacion.objects.create(numero= numero_cotizacion.get_next_value(),
                                                            cliente_id= encabezado['id_cliente'],
                                                            nombre_cliente= encabezado['nombre_cliente'],
                                                            descuento= encabezado['descuento']
                                                            )

                for value in detalle:
                    nueva_cotizacion.detallecotizacion_set.create(item_id= value['id_item'],
                                                                 cantidad_item= value['cantidad']
                                                                    )

                nueva_cotizacion.save()

                return JsonResponse({
                    'NoCotizacion':str(nueva_cotizacion.agnio)+'-'+str(nueva_cotizacion.numero),
                    'fecha':nueva_cotizacion.fecha_hora.strftime('%Y-%m-%d'),
                    'hora':nueva_cotizacion.fecha_hora.strftime('%I:%M:%S %p'),
                })

        except Exception as e :

            print('error',e)
            return Http404()

@login_required
def modificar_cotizacion(request):

    if request.method == 'GET':

        return  render(request, 'formulario_crear_cotizacion.html', {'form':FormCrearCotizacion})

    else:

        datos_cotizacion =  json.loads(request.body)

        encabezado= datos_cotizacion['encabezado']
        detalle= datos_cotizacion['detalle']
        noCotizacion= encabezado['noCotizacion']

        agnio= noCotizacion[0:4]
        print(agnio)
        numero= noCotizacion[5:]
        print(numero)

        cotizacion = get_object_or_404(Cotizacion, agnio= agnio, numero= numero)

        if encabezado['id_cliente'] == '':
            encabezado['id_cliente'] = None
        elif encabezado['nombre_cliente'] == '':
            encabezado['nombre_cliente'] = None

        try:
            with transaction.atomic():
                cotizacion.cliente_id= encabezado['id_cliente']
                cotizacion.nombre_cliente= encabezado['nombre_cliente']
                cotizacion.descuento= encabezado['descuento']

                list_items_json= list() 
                list_items_db= list()

                for value in detalle:
                    
                    list_items_json.append(int(value['id_item']))

                    cotizacion.detallecotizacion_set.update_or_create(item_id= value['id_item'],
                                                                cantidad_item= value['cantidad'])

                for element in cotizacion.detallecotizacion_set.all():

                    list_items_db.append(element.item.id)
                
                print(list_items_db != list_items_json)
                print('list_items_json',list_items_json)
                print('list_items_db',list_items_db)

                if list_items_db != list_items_json:
                    list_items_eliminar= [x for x in list_items_db if x not in set(list_items_json)]
                    print('list_items_eliminar',list_items_eliminar)

                    for item_listed in list_items_eliminar:
                        cotizacion.detallecotizacion_set.filter(item_id= item_listed).delete()

                cotizacion.save()

                return JsonResponse({
                                    'estatus': 'Los cambios han sido guardados.'
                                    })

        except Exception as e :

            print('error:', e)
            return Http404()