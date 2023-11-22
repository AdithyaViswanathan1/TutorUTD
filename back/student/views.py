from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets
from rest_framework import serializers as drf_serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student
from . import serializers as ota_serializers
from login.models import User
from tutor.models import Tutor, TutorSubjects
from rest_framework import status
from tutor.serializers import TutorSerializer, TutorSearchSerializer

class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = ota_serializers.EmptySerializer
    serializer_classes = {
        'make_appointment': ota_serializers.MakeAppointment,
        'get_tutors': ota_serializers.GetTutors,
        'cancel_appointment': ota_serializers.CancelAppointment,
        'add_favorite_tutor': ota_serializers.AddFavoriteTutor,
    }

    #Helper functions
    def list_to_dict(self, id_and_name):
        result = {}
        for tutor in id_and_name:
            id = tutor[0]
            name = tutor[1]
            result[name] = id
        return result
    
    @action(methods=['POST'], detail=True)
    def add_hours(self, request):
        return Response('This is a placeholder.')
    
    @action(methods=['POST'], detail=False)
    def make_appointment(self, request):
        serializer = self.get_serializer(data=request.data)
        return Response('This is a placeholder.')

    @action(methods=['POST'], detail=True)
    def cancel_appointment(self, request):
        return Response('This is a placeholder.')

    @action(methods=['GET', 'PUT'], detail=False)
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
        return Response({"Result": result}, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True)
    def add_favorite_tutor(self, request):
        return Response('This is a placeholder.')
    
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
