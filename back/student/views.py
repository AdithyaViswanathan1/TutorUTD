from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from rest_framework import viewsets, status
from rest_framework import serializers as drf_serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student
from . import serializers as ota_serializers
from appointments.models import Appointments
from login.models import User
from tutor.models import Tutor, TutorSubjects
from rest_framework import status
from tutor.serializers import TutorSerializer, TutorSearchSerializer
from tutor.models import Tutor
from student.models import Favorite_Tutors
from datetime import datetime

import json

class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = ota_serializers.EmptySerializer
    serializer_classes = {
        'make_appointment': ota_serializers.MakeAppointment,
        'get_tutors': ota_serializers.GetTutors,
        'cancel_appointment': ota_serializers.CancelAppointment,
        'add_favorite_tutor': ota_serializers.AddFavoriteTutor,
        'remove_favorite_tutor': ota_serializers.RemoveFavoriteTutor,
        'get_favorite_tutors': ota_serializers.GetFavoriteTutors,
        'get_appointments': ota_serializers.GetAppointments,
        'get_total_hours': ota_serializers.GetTotalHours,
    }

    #Helper functions
    def list_to_dict(self, id_and_name):
        result = {}
        for tutor in id_and_name:
            id = tutor[0]
            name = tutor[1]
            result[name] = id
        return result
    
    @action(methods=['POST'], detail=False)
    def make_appointment(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            dates = request.data.get('dates')
            student_id = request.data.get('student_id')
            tutor_id = request.data.get('tutor_id')
            student = Student.objects.get(student=student_id)
            tutor = Tutor.objects.get(tutor=tutor_id)
            for date in dates:
                # dates passed in are strings, not datetime objects
                format = "%a %b %d %Y.%H:%M %p"
                date = datetime.strptime(date, format)
                Appointments.objects.create(student=student, 
                                           tutor=tutor,
                                           time=date,
                                           location=request.data.get('location'),
                                           course=request.data.get('course'))
            return Response(status=status.HTTP_201_CREATED, data='Created successfully.')
        
        except drf_serializers.ValidationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Failed to make appointment: ' + str(e))

    @action(methods=['POST',], detail=False)
    def get_appointments(self, request):
        id = request.data['id']
        apps = Appointments.objects.filter(student_id=id,completed=False).order_by('time').values()
        
        if len(apps) == 0:
            return Response(apps, status=status.HTTP_204_NO_CONTENT)
        else:
            for obj in apps:
                format = "%a %b %d %Y.%H:%M %p"
                obj['time'] = obj['time'].strftime(format)

                student_id = obj['student_id']
                tutor_id = obj['tutor_id']

                student_name = User.objects.get(id=student_id).full_name
                tutor_name = User.objects.get(id=tutor_id).full_name
                obj['student_name'] = student_name
                obj['tutor_name'] = tutor_name
                
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
        
    @action(methods=['GET', 'POST'], detail=False)
    def tutor_search(self, request):
        # Search by course prefix only
        if "course_prefix" in request.data.keys() and "course_number" not in request.data.keys():
            prefix = request.data['course_prefix'].lower()
            # get tutor_id of matching prefix
            tutor_ids = TutorSubjects.objects.filter(subject__icontains=prefix).values_list('tutor_id', flat=True).distinct()
        # Search by course prefix and number
        elif "course_prefix" in request.data.keys() and "course_number" in request.data.keys():
            prefix = request.data['course_prefix'].lower()
            number = str(request.data['course_number'])
            search_string = f"{prefix} {number}"
            # get tutor_id of matching prefix
            tutor_ids = TutorSubjects.objects.filter(subject__iexact=search_string).values_list('tutor_id', flat=True).distinct()
        # search by tutor_name (partial or full)
        elif "tutor_name" in request.data.keys():
            name = request.data['tutor_name']
            # get tutor id and full_name from tutor_name
            tutor_ids = User.objects.filter(full_name__icontains=name,user_type="tutor").values_list("id").distinct()
        elif len(request.data) == 0:
            # list all tutors in the system
            tutor_ids = User.objects.filter(user_type="tutor").values_list('id')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # get tutor objects from previous ids and return only relevant fields (using serializer) and return as list of dictionaries
        tutor_objects = Tutor.objects.filter(pk__in=tutor_ids)
        result = []
        for tutor in tutor_objects:
            serial = TutorSearchSerializer(tutor)
            result.append(serial.data)    
        return Response(result, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=False)
    def add_favorite_tutor(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            tutor_id = request.data.get('tutor_id')
            student_id = request.data.get('student_id')
            tutor = Tutor.objects.get(tutor=tutor_id)
            student = Student.objects.get(student=student_id)
            Favorite_Tutors.objects.create(student=student, tutor=tutor)
            return Response(status=status.HTTP_201_CREATED, data='Added favorite tutor succesfully.')
        except drf_serializers.ValidationError as v:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Failed to add favorite tutor: ' + str(v))
    
    @action(methods=['DELETE'], detail=False)
    def remove_favorite_tutor(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            tutor_id = request.data.get('tutor_id')
            student_id = request.data.get('student_id')
            tutor = Tutor.objects.get(tutor=tutor_id)
            student = Student.objects.get(student=student_id)
            Favorite_Tutors.objects.filter(tutor=tutor, student=student).delete()
            return Response(status=status.HTTP_200_OK, data='Removed favorite tutor successfully')
        except Favorite_Tutors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Could not find favorite tutor.')
        
    @action(methods=['GET', 'POST'], detail=False)
    def get_favorite_tutors(self, request):
        serializer = self.get_serializer(data=request.data)
        student_id = request.data.get('student_id')

        try:
            student = Student.objects.get(student=student_id)
            favorite_tutors = Favorite_Tutors.objects.filter(student=student).values('tutor_id')
            tutor_data = []

            for tutor in favorite_tutors:
                q_set = Tutor.objects.get(tutor=tutor.get('tutor_id'))
                dict_q_set = model_to_dict(q_set)
                tutor_data.append(dict_q_set)
    
            return Response(status=status.HTTP_200_OK, data=tutor_data)
        except Favorite_Tutors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data='No favorite tutors found.')
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Student could not be found!!')
        
    @action(methods=['GET', 'POST'], detail=False)
    def get_total_hours(self, request):
        serializer = self.get_serializer(data=request.data)
        student_id = request.data.get('student_id')
        try: 
            hours = Student.objects.get(student=student_id).total_hours
            return Response(status=status.HTTP_200_OK, data=hours)
        except(Student.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND, data='Student not found.')


    
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
