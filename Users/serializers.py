from rest_framework import serializers
from .models import Account, TypeAccount, TypeLogin, Rol, TypeDoc


class AccountSerializer(serializers.ModelSerializer):
    """ User Serializer """
    class Meta:
        model = Account
        exclude = ['password']


class RegisterSerializer(serializers.ModelSerializer):
    """ Register Serializer """
    class Meta:
        model = Account
        exclude = ['date_create']
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
        fields = [
            'id',
            'name'
        ]


class TypeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAccount
        fields = [
            'id',
            'name'
        ]


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = [
            'id',
            'name'
        ]


class TypeDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDoc
        fields = [
            'id',
            'name'
        ]

