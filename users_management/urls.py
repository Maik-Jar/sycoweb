from django.urls import path
from . import views

urlpatterns= [path('user/', views.userpage, name='user'),
              path('login/', views.user_login, name='login'),
]