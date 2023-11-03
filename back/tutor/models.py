from django.db import models
from login.models import User

# Create your models here.
class Tutor(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)  # Field name made lowercase.
    total_hours = models.IntegerField(blank=True,default=0)
    subject_list = models.CharField(max_length=200, blank=True, null=True)
    about_me = models.CharField(max_length=200, blank=True, null=True)
    hours = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.CharField(max_length=500, blank=True, null=True)
    background_checked = models.BooleanField(blank=True, default=False)
    available = models.BooleanField(blank=True, default=False)

    class Meta:
        managed = True
        db_table = 'tutor'
    
    def __str__(self):
        return f'Hi. My name is {self.full_name}. I teach these subjects {self.subject_list}'
