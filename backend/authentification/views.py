from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from authentification.serializers import RegisterSerializer


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
                'user': str(self.request.user).title(),
                'message': '. Ahora mismo estás autenticado'
            }
        return Response(content)


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
