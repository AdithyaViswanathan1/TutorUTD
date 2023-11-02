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
        student = Student()
        student.save()
    elif user_type=='tutor':
        tutor = Tutor(
            email=User.objects.get(email=email),
            full_name=full_name,
            total_hours=0,
            background_checked=False,
        )
        tutor.save()
    
        
    return user

# Attempted to remedy the above problem with these calls.
def create_student_profile():
    student = Student(
            total_hours=0
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
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = get_and_authenticate_user(**serializer.validated_data)
        # data = serializers.AuthUserSerializer(user).data
        # return Response(data=data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')

            # user = None
            # if '@' in email:
            #     try:
            #         user = User.objects.get(email=email)
            #     except ObjectDoesNotExist:
            #         pass

            # if not user:
            user = authenticate(email=email, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)

            return Response({'error': f'Invalid credentials {email}, {password}'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['POST',], detail=False)
    def student_register(self, request):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = create_user_account(**serializer.validated_data, user_type='student')
        # # DATA BEING PASSED IN WRONGLY HERE
        # #create_student_profile(**serializer.validated_data)
        # data = serializers.AuthUserSerializer(user).data
        # return Response(data=data, status=status.HTTP_201_CREATED)
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['POST',], detail=False)
    def tutor_register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data, user_type='tutor')
        # DATA ALSO BEING PASSED IN WRONG HERE
        tutor = create_tutor_profile(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)
    
    
    # @action(methods=['POST',], detail=False)
    # #@permission_classes([IsAuthenticated])
    # def logout(self, request):
    #     if request.user.is_authenticated:
    #         logout(request)
    #         request.user.auth_token.delete()
    #         data = {'success': 'Sucessfully logged out'}
    #         return Response(data=data, status=status.HTTP_200_OK)
    #     return Response('ERROR: NOT AUTHENTICATED')
    #     # if request.method == 'POST':
    #     #     try:
    #     #         # Delete the user's token to logout
    #     #         request.user.auth_token.delete()
    #     #         return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    #     #     except Exception as e:
    #     #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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