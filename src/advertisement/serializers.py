from urllib.parse import urlparse

from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from src.advertisement.models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(pk_field=HashidSerializerCharField(source_field='advertisement.Event.id'),
                                            read_only=True)
    domain = serializers.CharField()
    total = serializers.IntegerField()

    class Meta:
        model = Event
        fields = '__all__'


    # def to_representation(self, obj):
    #     print("objejje")
    #     print(obj)
    #
    #     response = {"domain": obj.domain,
    #                 "total": obj['total']}
    #     return response


class EventDetailSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(pk_field=HashidSerializerCharField(source_field='advertisement.Event.id'),
                                            read_only=True)

    domain = serializers.CharField()
    parameter = serializers.CharField()

    class Meta:
        model = Event
        fields = '__all__'


class EventDeserializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(pk_field=HashidSerializerCharField(source_field='advertisement.Event.id'),
                                            read_only=True)
    page_url = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Event
        fields = ('id', 'type', 'page_url')

    def create(self, validated_data):
        page_url = validated_data.pop('page_url')

        validated_data['domain'] = urlparse(str(page_url)).netloc
        validated_data['parameter'] = urlparse(str(page_url)).path
        return super(EventDeserializer, self).create(validated_data)



