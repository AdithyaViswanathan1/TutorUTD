from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Tutor
from rest_framework.response import Response
from rest_framework import status
from tutor.serializers import TutorSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from login.models import User

def say_hello(request):
    return HttpResponse('Hello world!!! This is the login endpoint.')

# GET list of tutors
class TutorList(APIView):
    def get(self, request):
        movies = Tutor.objects.all() # get list of all Movies from DB
        serializer = TutorSerializer(movies, many=True) # convert raw output to JSON structure
        return Response(serializer.data, status=status.HTTP_200_OK) # return JSON response

# POST new tutor
class TutorCreate(APIView):
    def post(self, request):
        serializer = TutorSerializer(data=request.data) # converts request to JSON response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # returns JSON response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorProfile(APIView):
    def get_tutor_by_token(self, token):
        try:
            userid = Token.objects.filter(key=token).values_list('user_id', flat=True).first()
            movie = Tutor.objects.get(pk=userid)
            return movie
        except Tutor.DoesNotExist:
            return Response({"Error": "Tutor Does Not Exist"},status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        token_key = request.data['token']
        tutor = self.get_tutor_by_token(token_key)
        serializer = TutorSerializer(tutor)
        name = User.objects.get(id=tutor.tutor_id).full_name
        print("FULL NAME GET", name, type(serializer.data))
        return Response(serializer.data)

class TutorProfileEdit(APIView):
    def get_tutor_by_token(self, token):
        try:
            userid = Token.objects.filter(key=token).values_list('user_id', flat=True).first()
            movie = Tutor.objects.get(pk=userid)
            return movie
        except Tutor.DoesNotExist:
            return Response({"Error": "Tutor Does Not Exist"},status=status.HTTP_404_NOT_FOUND)
    
    def without_keys(self, d, keys):
        return {x: d[x] for x in d if x not in keys}

    def put(self, request):
        try:
            print(type(request))
            token_key = request.data['token']
            tutor = self.get_tutor_by_token(token_key)

            #if name field is in request.data, then update name separately
            if "full_name" in request.data.keys():
                #print("FULL NAME", request.data['full_name'])
                tutor_id = tutor.tutor_id
                User.objects.filter(id=tutor_id).update(full_name=request.data['full_name'])

            # take all fields in request.data except token,full_name and update fields in tutor table with given user_id
            data = self.without_keys(request.data, ["token","full_name"])
            print("Request without token and full_name",data)

            serializer = TutorSerializer(tutor, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Success": "Profile Updated"}, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response({"Error": "Profile Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

# run command "python3 manage.py makemigrations" to execute this sql query
# query to add tutor
# name = input("name:")
# email = input("email:")
# password = input("password:")
# test = Tutor(full_name=name, email=email, password=password)
# test.save()

# RAW SQL COMMAND EXAMPLE (SELECT)
# for p in Tutor.objects.raw("SELECT * FROM tutor"):
#     print("tutor::",p.full_name,p.email)

# #UPDATE COMMAND EXAMPLE'
# query = 'update tutor set full_name="adith" WHERE full_name="adit";'
# Tutor.objects.raw(query)

# for p in Tutor.objects.raw("SELECT * FROM tutor"):
#     print("tutor::",p.full_name,p.email)


