from django.urls import path
from rest_framework import routers
from .views import TutorViewSet

router = routers.DefaultRouter()
router.register('tutor', TutorViewSet, basename='tutor')

urlpatterns = router.urls