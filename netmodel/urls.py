from rest_framework.routers import DefaultRouter
from netmodel.apps import NetmodelConfig
from netmodel.views import NetworkModelViewSet, ProductViewSet

app_name = NetmodelConfig.name

router = DefaultRouter()
router.register(r"netmodels", NetworkModelViewSet, basename="netmodel")
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = []

urlpatterns += router.urls
