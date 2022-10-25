from django.urls import path
from . import views

urlpatterns= [path('', views.homepage),
              path('gestion_impuestos/', views.gestion_impuestos, name='gestion impuestos'),

]