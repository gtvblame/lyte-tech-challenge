from rest_framework import routers
from eventbrite.views import EventViewSet

app_name = 'eventbrite'

router = routers.DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = router.urls
