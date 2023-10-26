from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutor

def say_hello(request):
    return HttpResponse('Hello world! This is the login endpoint.')

# run command "python3 manage.py makemigrations" to execute this sql query
# query to add tutor
# name = input("name:")
# email = input("email:")
# password = input("password:")
# test = Tutor(full_name=name, email=email, password=password)
# test.save()

# RAW SQL COMMAND EXAMPLE (SELECT)
for p in Tutor.objects.raw("SELECT * FROM tutor"):
    print("tutor::",p.full_name,p.email)

#UPDATE COMMAND EXAMPLE'
query = 'update tutor set full_name="adith" WHERE full_name="adit";'
Tutor.objects.raw(query)

for p in Tutor.objects.raw("SELECT * FROM tutor"):
    print("tutor::",p.full_name,p.email)
