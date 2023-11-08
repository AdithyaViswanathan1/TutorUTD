from django.db import models
from student.models import *
from tutor.models import *

class Appointments(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'appointments'

class AppointmentManager(models.Manager):
    def create(self, **kwargs):
        pass


