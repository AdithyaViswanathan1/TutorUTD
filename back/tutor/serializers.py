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
    
    def validate_email(self,value):
        if "@" not in value:
            raise serializers.ValidationError("ERROR: Email address not valid")
        else:
            return value
    
    def validate_full_name(self,value):
        if " " not in value:
            raise serializers.ValidationError("ERROR: Full Name should include first and last name separated by a space")
        else:
            return value