
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/', viewset=None, basename='appointments')

urlpatterns = router.urls