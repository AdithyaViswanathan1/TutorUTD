from django.urls import include, path
from rest_framework import routers
from . import views
from .views import AuthViewSet

router = routers.DefaultRouter()
router.register('api/auth', AuthViewSet, basename='auth')


urlpatterns = router.urls