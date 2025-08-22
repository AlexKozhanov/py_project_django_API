import django_filters

from netmodel.models import NetworkModel


class NetworkModelFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name="contact__city", lookup_expr="iexact")

    class Meta:
        model = NetworkModel
        fields = ("contact_city",)
