from django.core import mail
from django.conf import settings
from tutor.models import Tutor
from student.models import Student
from appointments.models import Appointments
from login.models import User
import datetime

def dailyEmailReminder(): #Sends emails to students and tutors that have appointments on today's date
    connection = mail.get_connection() #Establishes connection to mail server
    connection.open()
    
    #Grab Querysets of appointments that match today's date and have unique ids
    studentappointments = Appointments.objects.filter(time=datetime.date.today()).distinct("student_id")
    tutorappointments = Appointments.objects.filter(time=datetime.date.today()).distinct("tutor_id")
    
    #Send email to all students with appointment matching today's date
    if studentappointments.exists():
        for e in studentappointments: #For every student that has an appointment today
            message = "This is a reminder from TutorUTD that you have the following tutoring appointments today: \n \n"
            eStudentAppointments = Appointments.objects.filter(student_id=e.student_id).filter(time=datetime.date.today()) #grab student e's appointments for today
            for i in eStudentAppointments: #for each appointment today
                message + " Appointment at time " + i.time + " with tutor " + User.objects.get(pk=i.tutor_id).full_name + "\n" #add app. details to message
            mail.EmailMessage("Tutor UTD: Appointment Reminder",
                message,
                settings.EMAIL_HOST_USER,
                [User.objects.get(pk=e.student_id).email], 
                connection).send()
    
    #Send email to all tutors with appointment matching today's date
    if tutorappointments.exists():
        for e in tutorappointments:
            message = "This is a reminder from TutorUTD that you have the following tutoring appointments today: \n \n"
            eTutorAppointments = Appointments.objects.filter(tutor_id=e.tutor_id).filter(time=datetime.date.today())
            for i in eTutorAppointments:
                message + " Appointment at time " + i.time + " with student " + User.objects.get(pk=i.student_id).full_name + "\n"
            mail.EmailMessage("Tutor UTD: Appointment Reminder",
                message,
                settings.EMAIL_HOST_USER,
                [User.objects.get(pk=e.tutor_id).email], 
                connection).send()
    
    connection.close()