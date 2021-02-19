from rest_framework import generics, permissions
from rest_framework.response import Response

from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from .customSerializersAuthToken import CustomAuthTokenSerializer
from .serializers import AccountSerializer, RegisterSerializer, \
                        TypeLoginSerializer, TypeAccountSerializer, \
                        RolSerializer, TypeDocSerializer
from .models import TypeLogin, TypeAccount, Rol, TypeDoc, Account


class RegisterAPI(generics.GenericAPIView):
    """ API Register """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """ Create a Account: user"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": AccountSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    """ API Login """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ListTypeLogin(generics.GenericAPIView):
    """ Query API Login Types """

    def get(self, request):
        """ Login Types List"""
        type_login = TypeLogin.objects.all()
        type_login_json = TypeLoginSerializer(type_login, many=True)
        return Response(type_login_json.data)


class ListTypeAccount(generics.GenericAPIView):
    """ Query API Account Types """

    def get(self, request):
        """ Account Types List """
        type_account = TypeAccount.objects.all()
        type_account_json = TypeAccountSerializer(type_account, many=True)
        return Response(type_account_json.data)


class ListRol(generics.GenericAPIView):
    """ Query API Rol """

    def get(self, request):
        """ Roles List """
        rol = Rol.objects.all()
        rol_json = RolSerializer(rol, many=True)
        return Response(rol_json.data)


class ListTypeDoc(generics.GenericAPIView):
    """ Query API Doc Types """

    def get(self, request):
        """ Doc Types List """
        type_doc = TypeDoc.objects.all()
        type_doc_json = TypeDocSerializer(type_doc, many=True)
        return Response(type_doc_json.data)


class AccountDetail(generics.GenericAPIView):
    """ Get Specific Account/User"""

    def get(self, request, pk):
        account = Account.objects.get(pk=pk)
        account_json = AccountSerializer(account)
        return Response(account_json.data, status=200)
# class AccountSkillAPI(generics.GenericAPIView):
#     """ API Account Skill: Skill by user """
#
#     def post(self, request):
#         """ Create Account Skill """
#         account_skill_json = AccountSkillSerializer(data=request.data)  # Unmarshal
#         if account_skill_json.is_valid():
#             account_skill_json.save()
#             return Response(account_skill_json.data, status=201)
#         return Response(account_skill_json.errors, status=400)
#
#
# class AccountSkillList(generics.GenericAPIView):
#     """ API Account Skills: Skills by user """
#
#     def get(self, request, fk):
#         """ Filter all skills by user """
#         account_skills = Account.objects.get(id_account=fk).select_related()
#         account_skill_json = AccountSerializerExtra(account_skills, many=True)
#         return Response(account_skill_json.data, status=200)
