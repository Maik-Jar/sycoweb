from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Cotizacion

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