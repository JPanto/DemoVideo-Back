from rest_framework import serializers
from .models import Account, TypeAccount, TypeLogin, Rol, AccountSkill, TypeDoc


# User Serializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id_account',
            'username',
            'full_name',
            'email',
            'date_create',
            'gender',
            'id_city',
            'id_type_login',
            'id_type_user',
            'id_rol'
        )


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id_account',
            'username',
            'first_name',
            'email',
            'password',
            'gender',
            'id_city',
            'id_type_login',
            'id_type_account',
            'id_rol',
            'id_type_doc'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.create_user(validated_data['username'],
                                           email=validated_data['email'],
                                           first_name=validated_data['first_name'],
                                           password=validated_data['password']
                                           )
        return user


class TypeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLogin
        fields = (
            'id_type_login',
            'name'
        )


class TypeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAccount
        fields = (
            'id_type_account',
            'name'
        )


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = (
            'id_rol',
            'name'
        )


class TypeDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDoc
        fields = (
            'id_type_doc',
            'name'
        )


class AccountSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSkill
        fields = (
            'id_account',
            'id_skill'
        )
