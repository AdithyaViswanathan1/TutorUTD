from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
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

import json

class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = ota_serializers.EmptySerializer
    serializer_classes = {
        'make_appointment': ota_serializers.MakeAppointment,
        'get_tutors': ota_serializers.GetTutors,
        'cancel_appointment': ota_serializers.CancelAppointment,
        'add_favorite_tutor': ota_serializers.AddFavoriteTutor,
        'remove_favorite_tutor': ota_serializers.RemoveFavoriteTutor
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
            print(request.data)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            dates = request.data.get('dates')
            student_id = request.data.get('student_id')
            tutor_id = request.data.get('tutor_id')
            student = Student.objects.get(student=student_id)
            tutor = Tutor.objects.get(tutor=tutor_id)
            for date in dates:
                Appointments.objects.create(student=student, 
                                           tutor=tutor,
                                           time=date,
                                           location=request.data.get('location'),
                                           course=request.data.get('course'))
            return Response(status=status.HTTP_201_CREATED, data='Created successfully.')
        
        except drf_serializers.ValidationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Failed to make appointment: ' + str(e))

    @action(methods=['POST'], detail=True)
    def cancel_appointment(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response('This is a placeholder.')

    # Need to accept information from the client to filter through which
    # tutors to get. Hence, this must be a POST to accept data,
    # but this will not make any changes in the database.
    @action(methods=['GET', 'POST'], detail=False)
    def get_tutors(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response('This is a placeholder.')
        
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

    @action(methods=['POST'], detail=True)
    def add_favorite_tutor(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response('This is a placeholder.')
    
    @action(methods=['POST'], detail=False)
    def remove_favorite_tutor(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response('This is a placeholder')
    
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
