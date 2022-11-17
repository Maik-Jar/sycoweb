from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns= [path('gestion_tipodocumento/', views.gestion_tipodocumento, name='gestion tipo documento'),
              path('gestion_tipodocumento/crear_tipo_documento/', views.crear_tipodocumento, name='crear tipo documento'),
              path('gestion_tipodocumento/modificar_tipo_documento/<int:idtipodocumento>/', views.modificar_tipodocumento, name='modificar tipo documento'),
              path('gestion_tipodocuemtno/eliminar_tipo_documento/<int:idtipodocumento>/', views.eliminar_tipo_documento, name='eliminar tipo documento'),
              path('gestion_tipo_cliente/', views.gestion_tipo_cliente, name='gestion tipo cliente'),
              path('gestion_tipo_cliente/crear_tipo_cliente/', views.crear_tipo_cliente, name='crear tipo cliente'),
              path('gestion_tipo_cliente/modificar_tipo_cliente/<int:idtipo_cliente>', views.modificar_tipo_cliente, name='modificar tipo cliente'),
              path('gestion_tipo_cliente/eliminar_tipo_cliente/<int:idtipo_cliente>/', views.eliminar_tipo_cliente, name='eliminar tipo cliente'),
              path('gestion_clientes/', views.gestion_clientes, name='gestion clientes'),
              path('gestion_clientes/crear_cliente/', views.crear_cliente, name='crear cliente'),




]

urlpatterns += static(settings.STATIC_URL)