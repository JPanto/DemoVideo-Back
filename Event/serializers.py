from rest_framework import serializers
from .models import Event, StateEvent, EventUser


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            '__all__'
        )


class StateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateEvent
        fields = (
            '__all__'
        )


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = (
            '__all__'
        )

# TODO: Verificar serializer para obtener objetos participaciones
class EventFullSerializer(serializers.ModelSerializer):
    participations = EventUserSerializer(many=True, read_only=True)
    model = Event
    fields = [
        'id_event',
        'participations'
    ]


# class EventFullSerializer(serializers.ModelSerializer):
#     entries = EventUserSerializer()
#
#     class Meta:
#         model = Event
#         fields = [
#             'id_event',
#             'name',
#             'description',
#             'value',
#             'date_start',
#             'date_end',
#             'slug',
#             'skills'
#         ]