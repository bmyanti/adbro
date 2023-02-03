from drf_rw_serializers import viewsets
from django.db.models import Count
from django.db.models import Sum
from django_filters import rest_framework as rest_framework_filters

from src.advertisement.models import Event
from src.advertisement import filters, serializers


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    http_method_names = ['list', 'post', 'get']
    read_serializer_class = serializers.EventDetailSerializer
    write_serializer_class = serializers.EventDeserializer


class ListEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    http_method_names = ['list', 'get']
    read_serializer_class = serializers.EventSerializer
    search_fields = 'type'
    filter_backends = (rest_framework_filters.DjangoFilterBackend,)
    filterset_class = filters.EventFilter

    def get_queryset(self, **kwargs):
        events = Event.objects.all().values('domain')\
            .annotate(total=Count('domain')).order_by('-total')
        if events.count() > 10:
            events = events[:10]
            others = events[10:]
            context = super(ListEventViewSet, self).get_serializer_context()
            context['others'] = (others.aggregate(domain=Sum('total', field="domain"))['domain'])
        return events
