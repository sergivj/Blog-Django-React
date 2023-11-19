from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentification.infrastructure.viewsets.post_viewset import PostViewSet
from authentification.infrastructure.viewsets.user_viewset import UserViewSet, RegisterViewSet

from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet, basename='users')
router.register(r'register', RegisterViewSet, basename='register-user')

urlpatterns = [
    path('', include(router.urls)),
]
