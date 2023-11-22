from rest_framework import serializers
from tutor.models import Tutor, TutorAvail, TutorSubjects
from login.models import User
from login.serializers import UserSerializer

class EmptySerializer(serializers.Serializer):
    pass

class TutorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')
    times = serializers.SerializerMethodField('available_times')
    subjects = serializers.SerializerMethodField('get_subjects')

    def get_full_name(self, obj): 
        # print ('selffff   ', serializers)
        prof_obj = User.objects.get(id=obj.tutor_id)
        return prof_obj.full_name
    
    def available_times(self, obj):
        times = TutorAvail.objects.filter(tutor_id=obj.tutor_id).values_list('time', flat=True)
        return times
    
    def get_subjects(self, obj):
        subs = TutorSubjects.objects.filter(tutor_id=obj.tutor_id).values_list('subject', flat=True)
        return subs
    
    class Meta:
        model = Tutor
        #fields = '__all__'
        fields = ('tutor_id','full_name', 'times', 'subjects', 'total_hours','biography', 'profile_picture','background_checked','available')

    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data
    
    # def validate_email(self,value):
    #     if "@" not in value:
    #         raise serializers.ValidationError("ERROR: Email address not valid")
    #     else:
    #         return value
    
    # def validate_full_name(self,value):
    #     if " " not in value:
    #         raise serializers.ValidationError("ERROR: Full Name should include first and last name separated by a space")
    #     else:
    #         return value

class TutorAvailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorAvail
        fields = "__all__"

class TutorSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSubjects
        fields = "__all__"


class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('tutor_id','total_hours','full_name')

class TutorSearchSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')
    subjects = serializers.SerializerMethodField('get_subjects')

    def get_full_name(self, obj): 
        # print ('selffff   ', serializers)
        prof_obj = User.objects.get(id=obj.tutor_id)
        return prof_obj.full_name
    
    def get_subjects(self, obj):
        subs = TutorSubjects.objects.filter(tutor_id=obj.tutor_id).values_list('subject', flat=True)
        return subs
    
    class Meta:
        model = Tutor
        #fields = '__all__'
        fields = ('tutor_id', 'full_name', 'subjects', 'profile_picture')
