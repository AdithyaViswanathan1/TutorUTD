
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/appointments/', viewset=None, basename='appointments')

urlpatterns = router.urls