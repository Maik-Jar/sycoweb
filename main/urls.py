from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns= [path('home/', views.homepage, name='homepage'),
              path('signin/', views.signin, name= 'signin'),
              path('signout/', views.signout, name= 'signout'),
              path('product_and_services/', include('product_services_management.urls')),
              path('users_management/', include('users_management.urls')),

]