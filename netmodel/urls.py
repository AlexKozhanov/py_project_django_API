from rest_framework.routers import DefaultRouter
from netmodel.apps import NetmodelConfig
from netmodel.views import NetworkModelViewSet

app_name = NetmodelConfig.name

router = DefaultRouter()
router.register("", NetworkModelViewSet)

urlpatterns = []

urlpatterns += router.urls
