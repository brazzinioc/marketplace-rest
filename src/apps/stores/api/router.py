from rest_framework.routers import DefaultRouter
from apps.stores.api.views.storeview import StoreViewSet
from apps.stores.api.views.categoryview import CategoryViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories' )
router.register(r'stores', StoreViewSet, basename='stores')

urlpatterns = router.urls
