from django.db import models
from Skill.models import Skill
from Users.models import Account


class Event(models.Model):
    id_event = models.AutoField
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    value = models.IntegerField
    date_start = models.CharField(max_length=10)
    date_end = models.CharField(max_length=10)
    slug = models.SlugField(max_length=220)
    skills = models.ManyToManyField(Skill)
    entries = models.ManyToManyField(Account, through='EventUser')
    id_file = models.ForeignKey('Files.Files', on_delete=models.CASCADE)
    id_state = models.ForeignKey('StateEvent', on_delete=models.CASCADE)
    id_city = models.ForeignKey('Location.City', on_delete=models.CASCADE)
    id_user = models.ForeignKey('Users.Account', on_delete=models.CASCADE, related_name='events')


class StateEvent(models.Model):
    """ Event SubClass"""

    id_state_event = models.AutoField
    name = models.CharField(max_length=25)


class EventUser(models.Model):
    """ Class ManyToMany between Event and Account/User"""

    id_event_user = models.AutoField
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=10)
    id_file = models.ForeignKey('Files.Files', on_delete=models.CASCADE)
    id_event = models.ForeignKey('Event', on_delete=models.CASCADE)
    id_user = models.ForeignKey('Users.Account', on_delete=models.CASCADE)