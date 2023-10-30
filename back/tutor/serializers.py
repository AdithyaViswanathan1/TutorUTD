from rest_framework import serializers
from tutor.models import Tutor

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data
    
    # def validate_name(self,value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value