from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import UserModelSerializer, RegisterUserSerializer

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs) -> Response:
        """
        POST method for user registration
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserModelSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.create(user=user).key
        }, status=201)

class LoginAPIView(APIView):
    def post(self, request) -> Response:
        """
        POST method for login user and getting auth token
        """
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Неверные учетные данные'}, status=400)
        
class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:
        """
        POST method for logout from system and deleting auth token
        """
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
