from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True)
    password = models.CharField(verbose_name='Password', max_length=100, blank=True, null=False)
    full_name = models.CharField(verbose_name='Full Name', max_length=255, blank=True, null=False)
    
    #to discern if the user is a student or tutor
    USER_TYPE_CHOICES = (('student', 'Student'), ('tutor', 'Tutor'))
    user_type = models.CharField(default='student', max_length=7, choices=USER_TYPE_CHOICES)
    
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = [first_name, last_name, password, user_type]
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.user_type.upper()} - {self.email} - {self.first_name} {self.last_name} "