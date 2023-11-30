# from django.urls import path
# from tutor import views
# from tutor.views import TutorList, TutorCreate, TutorProfileEdit, TutorProfile

# urlpatterns = [
#     path('', views.say_hello),
#     path('list/', TutorList.as_view()),
#     path('create/', TutorCreate.as_view()),
#     path('profile/', TutorProfile.as_view()),
#     path('profile/edit/', TutorProfileEdit.as_view()),
# ]

from rest_framework.routers import SimpleRouter
from .views import TutorViewSet
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
router.register('', TutorViewSet, basename='tutor')

urlpatterns = router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)