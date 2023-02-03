from django_filters import rest_framework as filters

from src.advertisement.models import Event


class EventFilter(filters.FilterSet):
    type = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Event
        fields = []
