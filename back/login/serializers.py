from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from . import models
#from student import models as StudentModel
#from tutor import models as TutorModel


User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    
class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'auth_token')
        read_only_fields = ('id',)
    
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    pass


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


'''
class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'user_type')
        
        def validate_email(self, value):
            user = User.objects.filter(email=value)
            if user:
                raise serializers.ValidateError('Email already in use.')
            return BaseUserManager.normalize_email(value)
        
        def validate_password(self, value):
            password_validation.validate_password(value)
            return value
        
class TutorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'user_type')
        
        def validate_email(self, value):
            user = User.objects.filter(email=value)
            if user:
                raise serializers.ValidateError('Email already in use.')
            return BaseUserManager.normalize_email(value)
        
        def validate_password(self, value):
            password_validation.validate_password(value)
            return value
'''