from django.contrib.auth import authenticate
from rest_framework import serializers as serial
from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from . import serializers
from .serializers import StudentRegisterSerializer, TutorRegisterSerializer, UserLoginSerializer
from rest_framework.generics import CreateAPIView
from tutor.models import Tutor
from student.models import Student

User = get_user_model()

#HELPER FUNCTIONS
def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serial.ValidationError("Invalid username/password.")
    return user

def create_user_account(email, password, first_name="", last_name="", user_type="", **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, 
        password=password, 
        first_name=first_name,
        last_name=last_name, 
        user_type=user_type,
    )
    
    user.save()
    full_name = first_name + ' ' + last_name
    
    # TODO: FIX. Currently the error is that when trying to register,
    # the user gets saved but when trying to query the user object
    # it does not exist at the time of calling.
    if user_type=='student':
        student = Student(
            email=User.objects.only(email),
            full_name=full_name
        )
        student.save()
    elif user_type=='tutor':
        tutor = Tutor(
            email=User.objects.only(email),
            full_name=full_name,
            total_hours=0,
            background_checked=False,
        )
        tutor.save()
    
        
    return user

# Attempted to remedy the above problem with these calls.
def create_student_profile(email, full_name):
    student = Student(
            email=User.objects.only(email),
            full_name=full_name
        )
    student.save()
    return student

def create_tutor_profile(email, full_name, total_hours=0, background_checked=False):
    tutor = Tutor(
            email=User.objects.only(email),
            full_name=full_name,
            total_hours=total_hours,
            background_checked=background_checked,
        )
    tutor.save()
    return tutor


#AUTHENTICATION, LOGIN, REGISTER, LOGOUT FUNCTIONS
class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny,]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'student_register': serializers.StudentRegisterSerializer,
        'tutor_register': serializers.TutorRegisterSerializer,
    }
    queryset = ''

    @action(methods=['POST',], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)
    
    @action(methods=['POST',], detail=False)
    def student_register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data, user_type='student')
        # DATA BEING PASSED IN WRONGLY HERE
        create_student_profile(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)
    
    @action(methods=['POST',], detail=False)
    def tutor_register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data, user_type='tutor')
        # DATA ALSO BEING PASSED IN WRONG HERE
        tutor = create_tutor_profile(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)
    
    
    @action(methods=['POST',], detail=False)
    def logout(self, request):
        if request.user.is_authenticated:
            logout(request)
            request.user.auth_token.delete()
            data = {'success': 'Sucessfully logged out'}
            return Response(data=data, status=status.HTTP_200_OK)
        return Response('Logged Out')


    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()