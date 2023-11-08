
from rest_framework import serializers
from datetime import date, datetime

class MakeAppointment(serializers.Serializer):
    token = serializers.HiddenField(default='')
    tutor_id = serializers.IntegerField(required=True)
    start_time = serializers.TimeField(required=True)
    end_time = serializers.TimeField(required=True)
    date = serializers.DateField(required=True)
    location = serializers.CharField(max_length=100, default='online', required=False)

    class Meta:
        fields = ('token', 'tutor_id', 'start_time', 'end_time', 'date', 'location')
    
    # validates the date. the date passed in will be compared with today's date. 
    # if it occurs before, then it is invalid
    def _validate_date(self, data):
        date_obj = datetime.strptime(data, '%Y-%m-%d').date()
        return date_obj >= date.today()

    # takes in the time that the user passes in as well as
    # the validated date from above
    def _validate_time(self, *argv):
        if argv is None:
            return -1
        
        # argv = [start_time, end_time, date]
        start_time = datetime.strptime(argv[0], '%H:%M').time() 
        end_time = datetime.strptime(argv[1], '%H:%M').time()
        date_obj = datetime.strptime(argv[2], '%Y-%m-%d').date()
        
        if date_obj == date.today():
            return start_time > datetime.now().replace(second=0, microsecond=0).time() and end_time > start_time
        return end_time > start_time
    
    def validate(self, data):
        if int(data['tutor_id']) < 0:
            raise serializers.ValidationError(detail='Invalid tutor ID: '+ data['tutor_id'])
        print(data)
        if not self._validate_date(data['date']):
            raise serializers.ValidationError(detail='Invalid date provided. Must be on or after ' + str(date.today()))
        if not self._validate_time(data['start_time'], data['end_time'], data['date']): 
            raise serializers.ValidationError(detail='Invalid time received. Start time is ' + data['start_time'] + \
                                              ' and End time is ' + data['end_time'])
        # NYI, validate the token
        # if data['token'] == '':
        #     raise serializers.ValidationError(detail='No token received, please log in to the system.')
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

