from django.urls import path
from . import views
from rest_framework import routers
from .api import UserViewSets

route = routers.DefaultRouter()

route.register('api/users', UserViewSets, 'user')

urlpatterns= route.urls

# [path('user/', views.userpage, name='user'),
#               path('login/', views.user_login, name='login'),
# ]