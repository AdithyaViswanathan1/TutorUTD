
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from student.models import Student, Favorite_Tutors
from tutor.models import Tutor
from appointments.models import Appointments
from datetime import datetime
from .models import Student
from tutor.models import Tutor, TutorSubjects
from appointments.models import Appointments


def _validate_tutor(tutor_id):
        if tutor_id < 0:
            raise serializers.ValidationError(detail='Invalid tutor ID: '+ str(tutor_id))
        try:
            Tutor.objects.get(tutor=tutor_id)
        except Tutor.DoesNotExist:
            raise serializers.ValidationError('Tutor could not be found')
        
class MakeAppointment(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)
    dates = serializers.ListField(required=True, child=serializers.DateTimeField(required=True, 
                                                                  input_formats=["%Y-%m-%dThh:mm", "iso-8601"]))
    location = serializers.CharField(max_length=20, required=False)
    course = serializers.CharField(max_length=20, required=False)

    class Meta:
        fields = ('student_id', 'tutor_id', 'dates', 'location')

    def _validate_date(self, request: datetime):
        today = datetime.today().date()
        return request.date() >= today
    
    # the date has already been validated at this point
    def _validate_time(self, request: datetime):
        if (datetime.today().date() == request.date()):
            return request.time() > datetime.now().time()
        # the time passed in is just a start time, so any start time after today should be valid
        return True

    def _validate_times(self, requested_dates: list[datetime]):
        if not requested_dates:
            raise serializers.ValidationError(detail="No dates specified.")
        
        invalid_dates = []
        for request in requested_dates:
            if not self._validate_date(request):
                invalid_dates.append(request)
            elif not self._validate_time(request):
                invalid_dates.append(request)
        
        if invalid_dates:
            msg = 'The following times were invalid: '
            for date in invalid_dates:
                msg += str(date) + ', '
            msg = msg[0:len(msg)-2]
            raise serializers.ValidationError(detail=msg)
        
    def _validate_tutor(self, tutor_id):
        if tutor_id < 0:
            raise serializers.ValidationError(detail='Invalid tutor ID: '+ str(tutor_id))
        try:
            Tutor.objects.get(tutor=tutor_id)
        except Tutor.DoesNotExist:
            raise serializers.ValidationError('Tutor could not be found')
        
    def validate(self, data):
        try:
            _validate_tutor(data['tutor_id'])
            self._validate_times(data['dates'])
        except serializers.ValidationError as e:
            raise e 
        
        return data

class AddFavoriteTutor(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)

    class Meta:
        fields = ('student_id', 'tutor_id')

    def _already_exists(self, student_id, tutor_id):
        if Favorite_Tutors.objects.filter(student=student_id, tutor=tutor_id):
            raise serializers.ValidationError(detail='You have already favorited that tutor.')

    def validate(self, data):
        try:
            _validate_tutor(data['tutor_id'])
            self._already_exists(data['student_id'], data['tutor_id'])
        except serializers.ValidationError as e:
            raise e 
        
        return data

class RemoveFavoriteTutor(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)

    class Meta:
        fields = ('student_id', 'tutor_id')
    
    def _does_not_exist(self, student_id, tutor_id):
        try:
            favorite_tutor = Favorite_Tutors.objects.get(student=student_id, tutor=tutor_id)
        except Favorite_Tutors.DoesNotExist as dne:
            raise dne
    
    def validate(self, data):
        try:
            self._does_not_exist(data['student_id'], data['tutor_id'])
        except Favorite_Tutors.DoesNotExist as dne:
            raise dne
        
        return data

class GetFavoriteTutors(serializers.Serializer):
    student = serializers.IntegerField(required=True)

    class Meta:
        fields = ('student_id')        

class CancelAppointment(serializers.Serializer):
    appointment_id = serializers.IntegerField(required=True)
    student_id = serializers.IntegerField(required=True)
    class Meta:
        fields = ('student_id', 'appointment_id')

    def _appointment_exists(self, appointment_id, student_id):
        try:
            Appointments.objects.filter(id=appointment_id, student=student_id)
        except Appointments.DoesNotExist as dne:
            raise dne

    def validate(self, data):
        try:
            self._appointment_exists(data['appointment_id'], data['student_id'])
        except Appointments.DoesNotExist as dne:
            raise dne
        
        return data

class GetTutors(serializers.Serializer):
    course = serializers.CharField(required=True)
        
    # class Meta:
    #     fields = ('course')
    #course_number = serializers.CharField(required=True)
    
    class Meta:
        model = TutorSubjects
        fields = "__all__"

class GetAppointments(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)

    class Meta:
        model = TutorSubjects
        fields = "__all__"

class GetAppointments(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)

    class Meta:
        fields = ('student_id')

class EmptySerializer(serializers.Serializer):
    pass

