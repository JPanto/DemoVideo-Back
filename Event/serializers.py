from rest_framework import serializers
from .models import Event, StateEvent, EventSkill, EventUser


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        event = Event
        fields = (
            'id_event',
            'name',
            'description',
            'value',
            'date_start',
            'date_end',
            'slug',
            'id_file',
            'id_state',
            'id_city',
            'id_user'
        )


class StateEventSerializer(serializers.ModelSerializer):
    class Meta:
        state_event = StateEvent
        fields = (
            'id_state_event',
            'name'
        )


class EventSkillSerializer(serializers.ModelSerializer):
    class Meta:
        event_skill = EventSkill
        fields = (
            'id_event',
            'id_skill'
        )


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        event_user = EventUser
        fields = (
            'id_event_user',
            'description',
            'date',
            'id_file',
            'id_event',
            'id_user'
        )
