from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns= [path('home/', views.homepage, name='homepage'),
              path('signin/', views.signin, name= 'signin'),
              # path('signin/', TemplateView.as_view(template_name= 'index.html'), name= 'signin'),
              path('signout/', views.signout, name= 'signout'),
              path('product_and_services/', include('product_services_management.urls')),
              path('users_management/', include('users_management.urls')),
              path('customers_management/', include('customers_management.urls')),
              path('sales_point/', include('sales_point.urls')),

]