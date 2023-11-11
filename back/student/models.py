
from django.db import models
from login.models import User
from tutor.models import Tutor


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)  # Field name made lowercase.
    total_hours = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'student'
    
    # def __str__(self):
    #     return f'{self.student.first_name + " " + self.student.last_name}'


class Favorite_Tutors(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'favorite_tutors'
