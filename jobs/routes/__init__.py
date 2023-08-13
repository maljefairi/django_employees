from rest_framework.routers import DefaultRouter

from .jobs import JobViewSet

router = DefaultRouter()
router.register(r'job', JobViewSet, basename='job')

urlpatterns = router.urls
