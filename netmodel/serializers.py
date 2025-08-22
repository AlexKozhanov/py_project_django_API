from rest_framework.serializers import ModelSerializer
from drf_writable_nested import WritableNestedModelSerializer
from netmodel.models import NetworkModel, Products


# from netmodel.validators import (
#     FieldFillingValidator,
#     RelatedHabitValidator,
#     execution_time_validator
# )


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class NetworkModelCreateSerializer(WritableNestedModelSerializer, ModelSerializer):
    class Meta:
        model = NetworkModel
        fields = ("id", "type", "name", "hierarchy_level", "supplier", "contact_email", "contact_city", "arrears")


class NetworkModelSerializer(ModelSerializer):
    """
    Сериализатор для модели NetworkModel.
    """
    class Meta:
        model = NetworkModel
        fields = "__all__"
        read_only_fields = ("supplier", "arrears",)


class NetworkModelBaseSerializer(ModelSerializer):
    products = ProductSerializer(many=True, required=False)

    def get_country(self, obj):
        return obj.contacts.values_list("contact_city", flat=True).distinct()

    class Meta:
        model = NetworkModel
        fields = ("id", "type", "name", "contact_city", "products")
