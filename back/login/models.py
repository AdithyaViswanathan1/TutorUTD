from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user



class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=255, blank=True, null=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=255, blank=True, null=False)
    password = models.CharField(verbose_name='Password', max_length=100, blank=True, null=False)
    
    #to discern if the user is a student or tutor
    USER_TYPE_CHOICES = (('student', 'Student'), ('tutor', 'Tutor'))
    user_type = models.CharField(default='student', max_length=7, choices=USER_TYPE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [first_name, last_name, password, user_type]
    
    objects = UserManager()

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"