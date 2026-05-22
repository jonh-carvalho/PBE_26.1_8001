from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, PlaylistViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet)
router.register(r'playlists', PlaylistViewSet)
urlpatterns = router.urls