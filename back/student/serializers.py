
from rest_framework import serializers
from .models import Student
from tutor.models import Tutor, TutorSubjects
from appointments.models import Appointments


class MakeAppointment(serializers.ModelSerializer):
    student_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)
    start_time = serializers.TimeField(required=True)
    end_time = serializers.TimeField(required=True)
    date = serializers.DateField(required=True)
    online = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = Appointments
        fields = ('student_id', 'start_time', 'end_time', 'date')

class AddFavoriteTutor(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)

class CancelAppointment(serializers.Serializer):
    appointment_id = serializers.IntegerField(required=True)

class GetTutors(serializers.Serializer):
    #course_number = serializers.CharField(required=True)
    
    class Meta:
        model = TutorSubjects
        fields = "__all__"

class EmptySerializer(serializers.Serializer):
    pass

