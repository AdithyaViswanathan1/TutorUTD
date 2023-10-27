
from rest_framework import serializers
from .models import Tutor

class TutorSerializer(serializers.Serializer):
    tutorid = serializers.IntegerField()  # Field name made lowercase.
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    subject_list = serializers.CharField(max_length=100)
    about_me = serializers.CharField(max_length=100)
    hours = serializers.CharField(max_length=100)
    profile_picture = serializers.CharField()
    total_hours = serializers.IntegerField()
    background_checked = serializers.IntegerField()
    available = serializers.IntegerField()

