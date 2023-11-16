from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentification.application.serializers.user_serializer import UserSerializer
from authentification.application.services.user_service import UserService


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'], url_path='get-user')
    def get_user(self, request):
        user_service = UserService()
        user = user_service.get_user_by_username(request.username)
        serializer = UserSerializer(user)
        return serializer.data

    @action(detail=True, methods=['get'], url_path='get-user-by-id')
    def get_user_by_id(self, id):
        user_service = UserService()
        user = user_service.get_user_by_id(id)
        serializer = UserSerializer(user)
        return serializer.data

    @action(detail=False, methods=['post'], url_path='register-user')
    def register_user(self, request):
        self.permission_classes = ()
        user_service = UserService()
        user = user_service.create_user(request.user)
        serializer = UserSerializer(user)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

    @action(detail=False, methods=['post'], url_path='logout-user')
    def logout_user(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': e})

    @action(detail=False, methods=['get'], url_path='home')
    def home(self, request):
        content = {
            'user': self.get_user(request.user),
            'message': '. Ahora mismo estás autenticado'
        }

        return Response(content)
