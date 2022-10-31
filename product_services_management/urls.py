from django.urls import path
from . import views

urlpatterns= [path('gestion_impuestos/', views.gestion_impuestos, name='gestion impuestos'),
              path('crear_impuesto/', views.crear_impuesto, name='crear impuesto'),
              path('gestion_impuestos/modificar_impuesto/<int:idimpuesto>/', views.modificar_impuesto, name='modificar impuesto'),

]