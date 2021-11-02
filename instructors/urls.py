
from rest_framework.routers import SimpleRouter

from .views import InstructorViewSet

router = SimpleRouter()
router.register('', InstructorViewSet, basename="instructors")

urlpatterns = router.urls
