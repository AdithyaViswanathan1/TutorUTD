from django.db import models

# Create your models here.
class Tutor(models.Model):
    tutorid = models.AutoField(db_column='tutorID', primary_key=True, editable=False)  # Field name made lowercase.
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    subject_list = models.CharField(max_length=100, blank=True, null=True)
    about_me = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.TextField(blank=True, null=True)
    total_hours = models.IntegerField(blank=True, null=True)
    background_checked = models.IntegerField(blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'tutor'
    
    def __str__(self):
        return f'Hi. My name is {self.full_name}. I teach these subjects {self.subject_list}'
