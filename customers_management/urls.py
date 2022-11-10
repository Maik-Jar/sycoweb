from django.urls import path
from . import views

urlpatterns= [path('gestion_tipodocumento/', views.gestion_tipodocumento, name='gestion tipo documento'),
              path('gestion_tipodocumento/crear_tipo_documento/', views.crear_tipodocumento, name='crear tipo documento'),
              path('gestion_tipodocumento/modificar_tipo_documento/<int:idtipodocumento>/', views.modificar_tipodocumento, name='modificar tipo documento'),
              path('gestion_tipodocuemtno/eliminar_tipo_documento/<int:idtipodocumento>/', views.eliminar_tipo_documento, name='eliminar tipo documento'),
              path('gestion_clientes/', views.gestion_clientes, name='gestion clientes'),




]