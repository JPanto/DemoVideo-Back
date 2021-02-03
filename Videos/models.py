from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")


    def __str__(self):
        return self.name + ": " + str(self.videofile)
