from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'posts', views.PostListViewSet, basename='posts')

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api/', include(router.urls)),
    path('new-entry/', views.NewEntryViewSet.as_view({
         'post':'create',
         }), name='new-entry'),
]
