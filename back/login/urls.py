
from rest_framework import routers
from .views import AuthViewSet

router = routers.DefaultRouter()
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = router.urls