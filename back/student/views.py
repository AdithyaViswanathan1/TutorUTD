from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets
from rest_framework import serializers as drf_serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student
from . import serializers as ota_serializers
from tutor.models import Tutor

class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = ota_serializers.EmptySerializer
    serializer_classes = {
        'make_appointment': ota_serializers.MakeAppointment,
        'get_tutors': ota_serializers.GetTutors,
        'cancel_appointment': ota_serializers.CancelAppointment,
        'add_favorite_tutor': ota_serializers.AddFavoriteTutor,
    }
    
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

    @action(methods=['GET'], detail=False)
    def get_tutors(self, request):
        return Response('This is a placeholder.')

    @action(methods=['POST'], detail=True)
    def add_favorite_tutor(self, request):
        return Response('This is a placeholder.')
    
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
