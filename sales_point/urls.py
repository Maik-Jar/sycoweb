from django.urls import path
from . import views
#

urlpatterns= [path('gestion_cotizaciones/', views.gestion_cotizaciones, name='gestion cotizaciones'),
            path('gestion_cotizaciones/crear_cotizacion/', views.crear_cotizacion, name='crear cotizacion'),
            path('gestion_cotizaciones/modificar_cotizacion/', views.modificar_cotizacion, name='modificar cotizacion'),
            ]