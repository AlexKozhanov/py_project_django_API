from rest_framework.serializers import ModelSerializer

from netmodel.models import NetworkModel

# from netmodel.validators import (
#     FieldFillingValidator,
#     RelatedHabitValidator,
#     execution_time_validator
# )


class NetworkModelSerializer(ModelSerializer):
    """
    Сериализатор для модели NetworkModel.
    """

    class Meta:
        model = NetworkModel
        fields = "__all__"

        # exclude = ("send_indicator",)
        # validators = [
        #     FieldFillingValidator(
        #         "reward",
        #         "related_habit",
        #         "sign_of_a_pleasant_habit"
        #     ),
        #     RelatedHabitValidator("related_habit"),
        # ]
