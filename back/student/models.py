
from django.db import models
from login.models import User
from tutor.models import Tutor

class Student(models.Model):
    studentid = models.AutoField(db_column='studentID', primary_key=True)  # Field name made lowercase.
    full_name = models.CharField(max_length=100)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    total_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

class Favorite_Tutors(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutorid = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'favorite_tutors'
