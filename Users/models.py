from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    id_account = models.BigIntegerField(primary_key=True,
                                        error_messages={'unique': 'Esta identificación de usuario ya está registrada'})
    username = models.CharField(unique=True, max_length=40,
                                error_messages={'unique': 'Este nombre de usuario ya está registrado'})
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    gender = models.BooleanField(default=True, null=False)
    id_city = models.ForeignKey('Location.City', on_delete=models.CASCADE, null=False)
    id_type_login = models.ForeignKey('TypeLogin', on_delete=models.CASCADE, null=False)
    id_type_account = models.ForeignKey('TypeAccount', on_delete=models.CASCADE, null=False)
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE, null=False)
    id_type_doc = models.ForeignKey('TypeDoc', on_delete=models.CASCADE, null=False)

    REQUIRED_FIELDS = [
        'id_account'
    ]


class TypeLogin(models.Model):
    id_type_login = models.AutoField
    name = models.CharField(max_length=20)


class TypeAccount(models.Model):
    id_type_account = models.AutoField
    name = models.CharField(max_length=20)


class Rol(models.Model):
    id_rol = models.AutoField
    name = models.CharField(max_length=20)


class TypeDoc(models.Model):
    id_type_doc = models.AutoField
    name = models.CharField(max_length=20)


class AccountSkill(models.Model):
    id_account = models.ForeignKey('Account', on_delete=models.CASCADE)
    id_skill = models.ForeignKey('Skill.Skill', on_delete=models.CASCADE)
