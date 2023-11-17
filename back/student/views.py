from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework import serializers as drf_serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student
from . import serializers as ota_serializers
from appointments.models import Appointments
from tutor.models import Tutor

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

    @action(methods=['POST'], detail=False)
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
