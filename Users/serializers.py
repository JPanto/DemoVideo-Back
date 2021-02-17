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
            'id_type_account',
            'id_rol'
        )


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id_account',
            'username',
            'full_name',
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
        user = Account.objects.create_user(id_account=validated_data['id_account'],
                                           username=validated_data['username'],
                                           full_name=validated_data['full_name'],
                                           email=validated_data['email'],
                                           password=validated_data['password'],
                                           gender=validated_data['gender'],
                                           id_city=validated_data['id_city'],
                                           id_type_login=validated_data['id_type_login'],
                                           id_type_account=validated_data['id_type_account'],
                                           id_rol=validated_data['id_rol'],
                                           id_type_doc=validated_data['id_type_doc'],
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
