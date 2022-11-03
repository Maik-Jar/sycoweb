from django.urls import path
from . import views

urlpatterns= [path('gestion_impuestos/', views.gestion_impuestos, name='gestion impuestos'),
              path('gestion_impuestos/crear_impuesto/', views.crear_impuesto, name='crear impuesto'),
              path('gestion_impuestos/modificar_impuesto/<int:idimpuesto>/', views.modificar_impuesto, name='modificar impuesto'),
              path('gestion_impuestos/eliminar_impuesto/<int:idimpuesto>/', views.eliminar_impuesto, name='eliminar impuesto'),
              path('gestion_categorias/', views.gestion_categorias, name='gestion categorias'),
              path('gestion_categorias/crear_categoria/', views.crear_categoria, name='crear categoria'),
              path('gestion_categorias/modificar_categoria/<int:idcategoria>/', views.modificar_categoria, name='modificar categoria'),
              path('gestion_categorias/eliminar_categoria/<int:idcategoria>/', views.eliminar_categoria, name='eliminar categoria'),
              path('gestion_servicios/', views.gestion_servicios, name='gestion servicios'),
              path('gestion_servicios/crear_servicio/', views.crear_servicio, name='crear servicio'),
              path('gestion_servicios/modificar_servicio/<int:iditem>/', views.modificar_servicio, name='modificar servicio'),
              path('gestion_servicios/eliminar_servicio/<int:iditem>/', views.eliminar_servicio, name='eliminar servicio'),
]