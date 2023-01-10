from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = UserSerializer