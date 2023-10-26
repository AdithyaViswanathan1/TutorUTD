from django.db import models

class Student(models.Model):
    studentid = models.AutoField(db_column='studentID', primary_key=True)  # Field name made lowercase.
    full_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    total_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
