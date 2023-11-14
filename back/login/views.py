from django.contrib.auth import authenticate
from rest_framework import serializers as serial, viewsets, status
from django.core.exceptions import ImproperlyConfigured
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import serializers
from .serializers import StudentRegisterSerializer, TutorRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

#NEW; delete later?
from duo_client import Auth
from django.conf import settings
from django.shortcuts import redirect

def Duo_Enroll(user):
    #Verify Duo 2FA with DUO API
    duo = Auth(
        ikey = settings.CLIENT_ID,
        skey = settings.CLIENT_SECRET,
        host = settings.API_HOSTNAME
    )
    
    #enrolling users into Duo
    if not user.duo_data:
        enroll_response = duo.enroll(username=user.email)
        user.duo_data = enroll_response
        user.save()
        
    return Response({'enroll_url':user.duo_data['activation_barcode']}, status=status.HTTP_201_CREATED)


def Duo_Authenticate(user):
    #Verify Duo 2FA with DUO API
    duo = Auth(
        ikey = settings.CLIENT_ID,
        skey = settings.CLIENT_SECRET,
        host = settings.API_HOSTNAME
    )
    
    
    #enroll users if not enrolled in Duo Mobile
    if not user.duo_data:
        return Duo_Enroll(user)
    else:
        e_status = duo.enroll_status(user.duo_data['user_id'], user.duo_data['activation_code'])
        if e_status != 'success':
            return Duo_Enroll(user)
    
    #Duo authentication
    preauth_response = duo.preauth(username=user.email)
    auth_response = duo.auth(username=user.email, factor='push', device=preauth_response['devices'][0]['device'])
    
    #Duo Authentication succeeded
    if auth_response['result'] == 'allow':
        userId = user.id
        return Response({'user_id': userId}, status=status.HTTP_200_OK)







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

            if user != None:
                return Duo_Authenticate(user)
            '''
            if user and user.user_type=="student":
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            '''

            return Response({'error': f'Invalid credentials {email}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)
        
    @action(methods=['POST',], detail=False)
    def tutor_login(self, request):
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            #print("LOGIN: User typr", user.user_type)

            if user != None:
                return Duo_Authenticate(user)
            
            '''
            user and user.user_type=="tutor":
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            '''

            return Response({'error': f'Invalid credentials {email}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['POST',], detail=False)
    def student_register(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            serializer.get_obj_type("student")
            if serializer.is_valid():
                user = serializer.save()
                return Duo_Enroll(user)
                #return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['POST',], detail=False)
    def tutor_register(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            serializer.get_obj_type("tutor")
            if serializer.is_valid():
                user = serializer.save()
                return Duo_Enroll(user)
                #return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
    @action(methods=['POST',], detail=False)
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