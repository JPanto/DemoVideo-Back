from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Skill
from .serializers import SkillSerializer


class ListSkill(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        skill_json = SkillSerializer(skills, many=True)
        return Response(skill_json.data)
