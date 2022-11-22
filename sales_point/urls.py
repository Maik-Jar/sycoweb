from django.urls import path
from . import views
#

urlpatterns= [path('gestion_cotizaciones/', views.gestion_cotizaciones, name='gestion cotizaciones'),



]