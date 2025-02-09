from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer

CustomUser = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()  
    serializer_class = CustomUserSerializer 