from rest_framework import serializers
from .models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        skill = Skill
        fields = (
            'id_skill',
            'name'
        )