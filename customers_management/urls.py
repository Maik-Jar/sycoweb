from django.urls import path
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
              path('gestion_clientes/modificar_cliente/<int:id_cliente>/', views.modificar_cliente, name='modificar cliente'),
              path('gestion_clientes/eliminar_cliente/<int:id_cliente>/', views.eliminar_cliente, name='eliminar cliente'),
              path('obtener_cliente/<int:id_tipo_documento>/<str:no_documento>/', views.obtener_cliente, name='obtener cliente'),


]
