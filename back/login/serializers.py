from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from .models import User
from student.models import Student, Tutor
from rest_framework.authtoken.models import Token
from rest_framework import serializers
import re


user = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    obj_type = serializers.SerializerMethodField()
    my_type = None

    def get_obj_type(self, t):
        self.my_type = t
        #print("MY TYPE:",self.my_type)

    class Meta:
        model = User
        fields = "__all__"
        #fields = ['first_name', 'last_name', 'email', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User(
            email=validated_data['email'],
            full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.user_type = self.my_type
        user.save()
        print("MY TYPE = ")
        if self.my_type == "student":
            print("USER TYPE IS STUDENT")
            Student.objects.create(student=user,total_hours=0)
        else:
            Tutor.objects.create(tutor=user,total_hours=0)
        return user
    
    def validate_password(self,value):
        special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if len(value) < 8:
            raise serializers.ValidationError("Password is too short! Must be at least 8 characters.")
        elif not bool(re.search(r'[A-Z]', value)):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        elif special_chars.search(value) == None:
            raise serializers.ValidationError("Password must contain at least one special character.")
        else:
            return value


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    
class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'user_type', 'auth_token')
        read_only_fields = ('id', 'user_type',)
    
    def get_auth_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    pass


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'email', 'password', 'full_name', 'user_type')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'email', 'password', 'full_name')
        
        def create(self, validated_data):
            user = User(
                email=validated_data('email'),
            )
            user.set_password(validated_data('password'))
            user.save()
            return user
        
class TutorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'email', 'password', 'full_name')
        
        def create(self, validated_data):
            user = User(
                email=validated_data('email'),
            )
            user.set_password(validated_data('password'))
            user.save()
            return user