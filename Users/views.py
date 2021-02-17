from rest_framework import generics, permissions
from rest_framework.response import Response

from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from Users.customSerializersAuthToken import CustomAuthTokenSerializer
from Users.serializers import AccountSerializer, RegisterSerializer, \
                            TypeLoginSerializer, TypeAccountSerializer, \
                            RolSerializer, TypeDocSerializer
from .models import TypeLogin, TypeAccount, Rol, TypeDoc


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": AccountSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# List Type Login
class ListTypeLogin(generics.GenericAPIView):
    def get(self, request):
        type_login = TypeLogin.objects.all()
        type_login_json = TypeLoginSerializer(type_login, many=True)
        return Response(type_login_json.data)


# List Type Account
class ListTypeAccount(generics.GenericAPIView):
    def get(self, request):
        type_account = TypeAccount.objects.all()
        type_account_json = TypeAccountSerializer(type_account, many=True)
        return Response(type_account_json.data)


# List Rol
class ListRol(generics.GenericAPIView):
    def get(self, request):
        rol = Rol.objects.all()
        rol_json = RolSerializer(rol, many=True)
        return Response(rol_json.data)


# List Type Doc
class ListTypeDoc(generics.GenericAPIView):
    def get(self, request):
        type_doc = TypeDoc.objects.all()
        type_doc_json = TypeDocSerializer(type_doc, many=True)
        return Response(type_doc_json.data)
