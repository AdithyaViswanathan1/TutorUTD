from django.db import models
from login.models import User

# Create your models here.
class Tutor(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True, related_name="user")  # Field name made lowercase.
    total_hours = models.IntegerField(verbose_name="Total Hours Completed", blank=True,default=0)
    #subject_list = models.CharField(verbose_name="Subject List", max_length=1000, blank=True, null=True)
    subject_list = None
    biography = models.CharField(verbose_name="Biography", max_length=1000, blank=True, null=True)
    profile_picture = models.FileField(verbose_name="Profile Picture", upload_to="media/", blank=True, null=True)
    background_checked = models.BooleanField(verbose_name="Background Check Complete", blank=True, default=False)
    available = models.BooleanField(verbose_name="Is Available?", blank=True, default=False)
    #hours = models.CharField(verbose_name="Available Times", max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tutor'
    
    def __str__(self):
        return f'{self.tutor.full_name}'

class TutorAvail(models.Model):
    tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE)
    time = models.CharField(max_length=500, blank=True, null=False)

    def __str__(self):
        return f"{self.tutor} - {self.time}"
    
class TutorSubjects(models.Model):
    tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE)
    subject = models.CharField(max_length=500, blank=True, null=False)

    def __str__(self):
        return f"{self.tutor} - {self.subject}"
