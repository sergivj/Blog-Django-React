from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentification.application.serializers.user_serializer import UserSerializer
from authentification.application.use_cases.user_use_cases import UserUseCases


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = UserUseCases()

    @action(detail=True, methods=['get'], url_path='get-user')
    def get_user(self, request):
        self.permission_classes = (IsAuthenticated,)
        user = self.use_case.get_user_by_username(request.username)
        serializer = UserSerializer(user)
        return serializer.data

    @action(detail=True, methods=['get'], url_path='get-user-by-id')
    def get_user_by_id(self, user_id):
        self.permission_classes = (IsAuthenticated,)
        user = self.use_case.get_user_by_id(user_id)
        serializer = UserSerializer(user)
        return serializer.data

    @action(detail=False, methods=['post'], url_path='logout-user')
    def logout_user(self, request):
        self.permission_classes = (IsAuthenticated,)
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': e})

    @action(detail=False, methods=['get'], url_path='home')
    def home(self, request):
        self.permission_classes = (IsAuthenticated,)
        content = {
            'user': self.get_user(request.user),
            'message': '. Ahora mismo estás autenticado'
        }

        return Response(content)


class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = ()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = UserUseCases()

    @action(detail=False, methods=['post'], url_path='register-user')
    def register_user(self, request):
        self.permission_classes = ()
        user = self.use_case.create_user(request.data)
        return Response(user, status=status.HTTP_201_CREATED)
