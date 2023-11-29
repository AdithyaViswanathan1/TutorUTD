from tutor.models import Tutor
from student.models import Student
from appointments.models import Appointments

def dailyEmailReminder():
    if studentapp = appointments.objects.filter(time=datetime.date.today()).order_by("student"):
        currentStudentId = studentapp.first().student
        for e in studentapp:
            message = "This is a reminder from TutorUTD that you have the following tutoring appointments today: \n" 
            if e.student==currentStudentId:
                message + "Appointment at time " + e.time + " for course " + e.course + " at " + e.location + " with tutor " Tutor.objects.get(e.tutor).full_name + "\n"
            else:
                send_mail("Appointment Reminder",
                    message,
                    "FROM@EMAIL",
                    [Student.objects.get(pk=currentStudentId).email])
                currentStudentId = e.student
    
    if tutorapp = appointments.objects.filter(time=datetime.date.today()).order_by("tutor"):
        currentTutorId = tutorapp.first().tutor
        for e in tutorapp:
            if e.tutor==currentTutorId:
                message + "Appointment at time " + e.time + " for course " + e.course + " at " + e.location + " with student " Student.objects.get(e.tutor).full_name
            else:
                send_mail("Appointment Reminder",
                    message,
                    "FROM@EMAIL",
                    [Tutor.objects.get(pk=currentTutorId).email], 
                    get_connection())
                currentTutorId = e.tutor