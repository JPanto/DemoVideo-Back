from django.db import models


# Create your models here.

class Event(models.Model):
    id_event = models.AutoField
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    value = models.IntegerField
    date_start = models.CharField(max_length=10)
    date_end = models.CharField(max_length=10)
    slug = models.CharField(max_length=220)
    id_file = models.ForeignKey('Files.Files', on_delete=models.CASCADE)
    id_state = models.ForeignKey('StateEvent', on_delete=models.CASCADE)
    id_city = models.ForeignKey('Location.City', on_delete=models.CASCADE)
    id_user = models.ForeignKey('Users.Account', on_delete=models.CASCADE)


class StateEvent(models.Model):
    id_state_event = models.AutoField
    name = models.CharField(max_length=25)


class EventSkill(models.Model):
    id_event = models.ForeignKey('Event', on_delete=models.CASCADE)
    id_skill = models.ForeignKey('Skill.Skill', on_delete=models.CASCADE)


class EventUser(models.Model):
    id_event_user = models.AutoField
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=10)
    id_file = models.ForeignKey('Files.Files', on_delete=models.CASCADE)
    id_event = models.ForeignKey('Event', on_delete=models.CASCADE)
    id_user = models.ForeignKey('Users.Account', on_delete=models.CASCADE)