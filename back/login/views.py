from django.contrib.auth import authenticate
from rest_framework import serializers as serial
from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from . import serializers
from .serializers import StudentRegisterSerializer, TutorRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework.generics import CreateAPIView
from tutor.models import Tutor
from student.models import Student
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view


User = get_user_model()

#AUTHENTICATION, LOGIN, REGISTER, LOGOUT FUNCTIONS
class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny,]
    serializer_class = serializers.EmptySerializer
    # purpose: to get the right fields
    serializer_classes = {
        'student_login': serializers.UserLoginSerializer, 
        'tutor_login': serializers.UserLoginSerializer,
        'student_register': serializers.StudentRegisterSerializer,
        'tutor_register': serializers.TutorRegisterSerializer,
    }
    queryset = ''

    @action(methods=['POST',], detail=False)
    def student_login(self, request):
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            #print("LOGIN: User typr", user.user_type)

            if user and user.user_type=="student":
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, "id": user.id}, status=status.HTTP_200_OK)

            return Response({'error': f'Invalid credentials {email}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)
        
    @action(methods=['POST',], detail=False)
    def tutor_login(self, request):
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            #print("LOGIN: User typr", user.user_type)

            if user and user.user_type=="tutor":
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, "id": user.id}, status=status.HTTP_200_OK)

            return Response({'error': f'Invalid credentials {email}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['POST',], detail=False)
    def student_register(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            serializer.get_obj_type("student")
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['POST',], detail=False)
    def tutor_register(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            serializer.get_obj_type("tutor")
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # from rest_framework.permissions import IsAuthenticated
    # permission_classes = [IsAuthenticated]
    @action(methods=['POST',], detail=False)
    #@permission_classes([IsAuthenticated])
    def logout(self,request):
        if request.method == 'POST':
            try:
                # Delete the user's token to logout
                request.user.auth_token.delete()
                return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()