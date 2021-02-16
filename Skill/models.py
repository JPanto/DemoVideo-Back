from django.db import models


class Skill(models.Model):
    id_skill = models.AutoField
    name = models.CharField(max_length=20)
