
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Student

class StudentSerializer(ModelSerializer):
    studentid = serializers.IntegerField() 
    full_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    total_hours = serializers.IntegerField()

    # still being implemented.
