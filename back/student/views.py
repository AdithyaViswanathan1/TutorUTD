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
from tutor.models import Tutor
from student.models import Favorite_Tutors

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
        'get_appointments': ota_serializers.GetAppointments
    }
    
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
                Appointments.objects.create(student=student, 
                                           tutor=tutor,
                                           time=date,
                                           location=request.data.get('location'),
                                           course=request.data.get('course'))
            return Response(status=status.HTTP_201_CREATED, data='Created successfully.')
        
        except drf_serializers.ValidationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Failed to make appointment: ' + str(e))

    @action(methods=['DELETE'], detail=False)
    def cancel_appointment(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            appointment_id = request.data.get('appointment_id')
            student_id = request.data.get('student_id')
            student = Student.objects.get(student=student_id)
            Appointments.objects.get(id=appointment_id, student_id=student).delete()
            return Response(status=status.HTTP_200_OK, data='Successfully cancelled appointment.')
        except Appointments.DoesNotExist as dne:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Could not cancel appointment because it does not exist.')
        except Student.DoesNotExist as dne:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Student could not be found!')
            

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
    
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
