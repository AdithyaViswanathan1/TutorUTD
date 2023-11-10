
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from student.models import Student
from tutor.models import Tutor
from datetime import datetime

class MakeAppointment(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)
    dates = serializers.ListField(required=True, child=serializers.DateTimeField(required=True, 
                                                                  input_formats=["%Y-%m-%dThh:mm", "iso-8601"]))
    location = serializers.CharField(max_length=20, default='online', required=False)
    course = serializers.CharField(max_length=20, default='', required=False)

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
            Tutor.objects.get(tutor_id=tutor_id)
        except Tutor.DoesNotExist:
            raise serializers.ValidationError('Tutor could not be found')
        
    
    def validate(self, data):
        try:
            self._validate_tutor(data['tutor_id'])
            self._validate_times(data['dates'])
        except serializers.ValidationError as e:
            raise e 
        
        return data

class AddFavoriteTutor(serializers.Serializer):
    token = serializers.HiddenField(default='')
    tutor_id = serializers.IntegerField(required=True)

    class Meta:
        fields = ('token', 'tutor_id')

class RemoveFavoriteTutor(serializers.Serializer):
    token = serializers.HiddenField(default='')
    tutor_id = serializers.IntegerField(required=True)

    class Meta:
        fields = ('token', 'tutor_id')

class CancelAppointment(serializers.Serializer):
    appointment_id = serializers.IntegerField(required=True)
    token = serializers.CharField(max_length=40)
    class Meta:
        fields = ('appointment_id')

class GetTutors(serializers.Serializer):
    course = serializers.CharField(required=True)
    
    class Meta:
        fields = ('course')

class EmptySerializer(serializers.Serializer):
    pass

