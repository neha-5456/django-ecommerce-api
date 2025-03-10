
from django.urls import path
from .views import UserRegistrationView,CustomTokenObtainPairView , LogoutView
from rest_framework_simplejwt.views import (
  
    TokenRefreshView,
)
urlpatterns = [
    path('register',  UserRegistrationView.as_view() , name = 'register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='logout'),
    
]
