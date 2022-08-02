from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('parent', ParentViewSet)
router.register('school', SchoolViewSet)


urlpatterns = router.urls


