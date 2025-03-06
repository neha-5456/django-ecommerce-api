from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")  # Remove confirm_password before saving
        
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])  # Hash password
        user.is_active = True  
        user.save()  
        return user
    
        
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
       
        return token 
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data
    
    