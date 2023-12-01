from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Tutor, TutorAvail, TutorSubjects
from rest_framework.response import Response
from tutor.serializers import TutorSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from login.models import User
from appointments.models import Appointments
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from . import serializers
from login import serializers as ls
from student import serializers as ota_serializers
from rest_framework.decorators import action
from django.db.models import F
from student.models import Student
from django.core.files.storage import default_storage
from io import BytesIO
from django.core.exceptions import ImproperlyConfigured


class TutorViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny,]
    serializer_classes = {
        'get_profile': serializers.GetProfileSerializer, 
        'edit_profile': serializers.EmptySerializer,
        'edit_profile_picture': serializers.EditProfileSerializer
    }
    serializer_class = serializers.EmptySerializer
    # purpose: to get the right fields
    queryset = ''

    #HELPER METHODS
    def get_tutor_by_token(self, token):
        try:
            userid = Token.objects.filter(key=token).values_list('user_id', flat=True).first()
            movie = Tutor.objects.get(pk=userid)
            return movie
        except Tutor.DoesNotExist:
            return Response({"Error": "Tutor Does Not Exist"},status=status.HTTP_404_NOT_FOUND)
    
    def get_tutor_by_id(self, userid):
        try:
            movie = Tutor.objects.get(pk=userid)
            return movie
        except Tutor.DoesNotExist:
            return Response({"Error": "Tutor Does Not Exist"},status=status.HTTP_404_NOT_FOUND)
        
    def without_keys(self, d, keys):
        return {x: d[x] for x in d if x not in keys}
    
    def update_times(self, tutor, new_times):
        print("FOUND TIMES NEEDED TO BE UPDATED", new_times, type(new_times), tutor.tutor_id)
        # Delete current times for this tutor
        TutorAvail.objects.filter(tutor_id=tutor.tutor_id).delete()
        # Add new times to the database (for this tutor)
        for time in new_times:
            #check if it exists in current_times
            # if it does, ignore
            # if it does not, then add it to database with current tutor_id
            TutorAvail.objects.create(tutor=tutor,time=time)
            print(f"{time} ADDED to DB")
    
    def update_subjects(self, tutor, new_subjects):
        # Delete current subjects for this tutor
        TutorSubjects.objects.filter(tutor_id=tutor.tutor_id).delete()
        # Add new subjects to the database (for this tutor)
        for subject in new_subjects:
            TutorSubjects.objects.create(tutor=tutor,subject=subject)
            print(f"{subject} ADDED to DB")

    # API CALLS
    @action(methods=['POST',], detail=False)
    def get_profile(self, request):
        userid = request.data['id']
        tutor = self.get_tutor_by_id(userid)
        serializer = TutorSerializer(tutor)
        return Response(serializer.data)
    
    @action(methods=['POST',], detail=False)
    def get_appointments(self, request):
        id = request.data['id']
        apps = Appointments.objects.filter(tutor_id=id,completed=False).values()
        if len(apps) == 0:
            return Response(apps, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(apps, status=status.HTTP_200_OK)
    
    @action(methods=['POST',], detail=False)
    def cancel_appointment(self, request):
        appid = request.data['appointment_id']
        try:
            Appointments.objects.filter(id=appid).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['POST',], detail=False)
    def mark_app_as_complete(self, request):
        appid = request.data['appointment_id']
        try:
            # mark appointment as complete
            app = Appointments.objects.get(id=appid)
            if app.completed == True:
                raise Exception
            app.completed = True
            student_id = app.student_id
            tutor_id = app.tutor_id
            app.save()
            # add time to student and tutor's hours field
            s = Student.objects.get(student_id=student_id)
            s.total_hours = s.total_hours + 0.5
            s.save()
            t = Tutor.objects.get(tutor_id=tutor_id)
            t.total_hours = t.total_hours + 0.5
            t.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    @action(methods=['PUT',], detail=False)
    def edit_profile(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.method == 'PUT':
            try:
                print("entered first step")
                userid = int(request.data['tutor_id'])
                print(userid, type(userid))
                tutor = self.get_tutor_by_id(userid)
                tutor_id = tutor.tutor_id
                print("checking for full_name, hours, subject_list")

                #if name field is in request.data, then update name separately
                if "full_name" in request.data.keys():
                    #print("FULL NAME", request.data['full_name'])
                    User.objects.filter(id=tutor_id).update(full_name=request.data['full_name'])
                
                if "hours" in request.data.keys() and request.data['hours'] != None:
                    new_times = request.data['hours']
                    self.update_times(tutor, new_times)

                if "subject_list" in request.data.keys() and request.data['subject_list'] != None:
                    new_subjects = request.data['subject_list']
                    self.update_subjects(tutor, new_subjects)

                # take all fields in request.data except token,full_name and update fields in tutor table with given user_id
                data = self.without_keys(request.data, ["token","full_name","hours", "subject_list"])
                print("Request without token, full_name, hours, subject_list",data)

                serializer = TutorSerializer(tutor, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"Success": "Profile Updated"}, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
                # return Response({"Error": "Profile Update Failed"}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PUT',], detail=False)
    def edit_profile_picture(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.method == 'PUT':
            try:
                print("entered first step")
                userid = int(request.data['tutor_id'])
                print(userid, type(userid))
                tutor = self.get_tutor_by_id(userid)
                serializer = TutorSerializer(tutor, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"Success": "Profile Picture Updated"}, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()