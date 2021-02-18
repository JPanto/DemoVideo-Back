from django.conf.urls import url

from .views import ListSkill

urlpatterns = [
    url(r'^api/skill/$', ListSkill.as_view(), name='list_skill'),
]