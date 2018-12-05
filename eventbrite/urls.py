from rest_framework import routers
from eventbrite.views import DummyViewSet

app_name = 'eventbrite'

router = routers.DefaultRouter()
router.register('dummy', DummyViewSet, basename='dummy-basename')

urlpatterns = router.urls
