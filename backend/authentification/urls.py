from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentification.infrastructure.viewsets.post_viewset import PostViewSet
from authentification.infrastructure.viewsets.user_viewset import UserViewSet


from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
