from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser  
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import generics

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        print("CustomUserViewSet - list method")
        print("Queryset:", self.queryset)
        response = super().list(request, *args, **kwargs)
        print("Response data:", response.data)
        return response

    def create(self, request, *args, **kwargs):
        print("CustomUserViewSet - create method")
        print("Request data:", request.data)
        response = super().create(request, *args, **kwargs)
        print("Created user:", response.data)
        return response

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        print("CustomTokenObtainPairView - post method")
        print("Request data:", request.data)
        response = super().post(request, *args, **kwargs)
        print("Token response:", response.data)
        return response

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        print("RegisterUserView - post method")
        print("Request data:", request.data)
        response = super().post(request, *args, **kwargs)
        print("Created user:", response.data)
        return response
