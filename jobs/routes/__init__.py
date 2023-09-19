from rest_framework.routers import DefaultRouter

from .jobs import JobViewSet, JobLocationsView

router = DefaultRouter()
router.register(r'job', JobViewSet, basename='job')
router.register(r'job-locations', JobLocationsView, basename='job_locations')


urlpatterns = router.urls
