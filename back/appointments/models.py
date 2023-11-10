from django.db import models
from student.models import *
from tutor.models import *
from datetime import datetime

class Appointments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    time = models.DateTimeField(null=False, default=datetime.min)
    location = models.CharField(max_length=100)
    course = models.CharField(max_length=20, null=True, default='None')

    class Meta:
        managed = True
        db_table = 'appointments'



