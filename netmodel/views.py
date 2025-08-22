from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
# Models
from netmodel.models import NetworkModel, Products
from netmodel.serializers import (
    ProductSerializer,
    NetworkModelCreateSerializer,
    NetworkModelSerializer,
    NetworkModelBaseSerializer)
# Не знаю из какой группы
from netmodel.filters import NetworkModelFilter
# Swagger
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from users.permissions import IsRelatedPerson


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения списка"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения конкретной"
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для создания"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для обновления информации"
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для частичного изменения информации"
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для удаления"
    ),
)
class NetworkModelViewSet(viewsets.ModelViewSet):

    queryset = NetworkModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkModelFilter

    def get_permissions(self):
        if self.action != "list":
            self.permission_classes = (IsRelatedPerson,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "create":
            self.serializer_class = NetworkModelCreateSerializer
        elif self.action == "list":
            self.serializer_class = NetworkModelBaseSerializer
        else:
            self.serializer_class = NetworkModelSerializer
        return super().get_serializer_class()


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
