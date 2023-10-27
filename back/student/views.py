from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

    @action(methods=['POST'], detail=False)
    def add_hours(self, request):
        pass
    
    @action(methods=['POST',], detail=False)
    def make_appointment(self, request):
        pass
