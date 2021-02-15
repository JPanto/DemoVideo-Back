from django.db import models
from django.contrib.auth.models import User


class Files(models.Model):
    id_file = models.AutoField
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    path = models.FileField(upload_to='files/', null=False, verbose_name="")
    type = models.ForeignKey('TypeFile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ": " + str(self.path)


class TypeFile(models.Model):
    id_type_file = models.AutoField
    name = models.CharField(max_length=15)
