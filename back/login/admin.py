from django.contrib import admin
# from login.models import User

# # Register your models here.
# admin.site.register(User)

from django.contrib.auth import get_user_model


admin.site.register(get_user_model())