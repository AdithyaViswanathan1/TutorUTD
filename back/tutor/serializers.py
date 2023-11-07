from rest_framework import serializers
from tutor.models import Tutor
from login.models import User
from login.serializers import UserSerializer

class TutorSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('user_info')

    def user_info(self, obj): 
        # print ('selffff   ', serializers)
        prof_obj = User.objects.get(id=obj.tutor_id)
        return {'full_name':prof_obj.full_name}
    
    class Meta:
        model = Tutor
        #fields = '__all__'
        fields = ('tutor_id','user','total_hours','subject_list','biography','hours','profile_picture','background_checked','available')

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
