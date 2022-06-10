from rest_framework.routers import DefaultRouter
from about.viewset import AboutViewSet

router = DefaultRouter()
router.register('about', AboutViewSet)

