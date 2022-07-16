from rest_framework.routers import DefaultRouter

from caterings.views import CateringViewSet, BookCateringViewSet

router = DefaultRouter()
router.register(r'caterings', CateringViewSet)
router.register(r'book_caterings', BookCateringViewSet)

urlpatterns = router.urls
