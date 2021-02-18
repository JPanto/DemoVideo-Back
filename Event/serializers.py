from rest_framework import serializers
from .models import Event, StateEvent, EventSkill, EventUser


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
            'id_state_event',
            'name'
        )


class EventSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSkill
        fields = (
            'id_event',
            'id_skill'
        )


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = (
            'id_event_user',
            'description',
            'date',
            'id_file',
            'id_event',
            'id_user'
        )
