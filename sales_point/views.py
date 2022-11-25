from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from .models import Cotizacion
from .forms import FormCrearCotizacion, FormCrearDetalleCotizacion

# Create your views here.

@login_required
def gestion_cotizaciones(request):

    if request.method == 'GET':
        
        cotizacion= Paginator(Cotizacion.objects.all().order_by('agnio', 'numero'), 10)

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



        