from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import RegisterSerializer , MyTokenObtainPairSerializer
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class =  RegisterSerializer

    def post(self , request ,  *args, **kwargs):
        serializer =  self.get_serializer(data =  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
class LogoutView(APIView):
     permission_classes = [IsAuthenticated]  # Ensure only logged-in users can logout

     def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token
            return Response({"message": "Logout successful!"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        