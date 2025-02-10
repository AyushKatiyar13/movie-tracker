from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet
from movies import views

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('api/movies/', views.MovieViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
