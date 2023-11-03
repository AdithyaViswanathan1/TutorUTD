from django.db import models
from login.models import User

# Create your models here.
class Tutor(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)  # Field name made lowercase.
    total_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tutor'
    
    def __str__(self):
        return f'Hi. My name is {self.full_name}. I teach these subjects {self.subject_list}'
