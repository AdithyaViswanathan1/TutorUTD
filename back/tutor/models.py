from django.db import models

# Create your models here.
class Tutor(models.Model):
    tutorid = models.AutoField(db_column='tutorID', primary_key=True)  # Field name made lowercase.
    full_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    subject_list = models.CharField(max_length=100, blank=True, null=True)
    about_me = models.CharField(max_length=100, blank=True, null=True)
    hours = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.TextField(blank=True, null=True)
    total_hours = models.IntegerField(blank=True, null=True)
    background_checked = models.IntegerField(blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tutor'
