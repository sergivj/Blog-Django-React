from django.core.serializers import get_serializer
from django.forms import model_to_dict
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from authentification.serializers import RegisterSerializer, PostsSerializer, AuthorSerializer, UserSerializer, NewEntrySerializer

from authentification.models import Post, User


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    def get(self, request, **kwargs):
        try:
            return model_to_dict(User.objects.get(username=request.username))
        except Exception as e:
            return {'error': e}


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
                'user': UsersViewSet().get(request.user),
                'message': '. Ahora mismo estás autenticado'
            }

        return Response(content)


class PostListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = list(Post.objects.all())
    serializer_class = PostsSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-date_posted')
        return queryset


class NewEntryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostsSerializer

    def create(self, request, **kwargs):
        try:
            serializer = NewEntrySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=self.request.user)
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': serializer.errors})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = ()

    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            print(serializer.is_valid())

            if serializer.is_valid():
                response = serializer.create(serializer.validated_data)
                try:
                    if response['error']:
                        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': response['error']})
                except:
                    return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Datos inválidos'})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': e})
