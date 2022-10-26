from django.urls import path
from . import views

urlpatterns= [path('gestion_impuestos/', views.gestion_impuestos, name='gestion impuestos'),
              path('formulario_impuesto/', views.form_impuesto, name='formulario impuestos'),

]