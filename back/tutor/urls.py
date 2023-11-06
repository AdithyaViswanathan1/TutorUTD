from django.urls import path
from tutor import views
from tutor.views import TutorList, TutorCreate, TutorProfileEdit, TutorProfile

urlpatterns = [
    path('', views.say_hello),
    path('list/', TutorList.as_view()),
    path('create/', TutorCreate.as_view()),
    path('profile/', TutorProfile.as_view()),
    path('profile/edit/', TutorProfileEdit.as_view()),
]
