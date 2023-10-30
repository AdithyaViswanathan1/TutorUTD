from django.urls import path
from tutor import views
from tutor.views import TutorList

urlpatterns = [
    path('', views.say_hello),
    path('list/', TutorList.as_view())
]