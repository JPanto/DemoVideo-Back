from django.conf.urls import url
from Users.views import RegisterAPI, LoginAPI, ListTypeLogin, \
                        ListTypeAccount, ListRol, ListTypeDoc
from knox import views as knox_views


urlpatterns = [
    url(r'^api/register/$', RegisterAPI.as_view(), name='register'),
    url(r'^api/login/$', LoginAPI.as_view(), name='login'),
    url(r'^api/logout/$', knox_views.LogoutView.as_view(), name='logout'),
    url(r'^api/logoutall/$', knox_views.LogoutAllView.as_view(), name='logoutall'),
    url(r'^api/typelogin/$', ListTypeLogin.as_view(), name='list_type_login'),
    url(r'^api/typeaccount/$', ListTypeAccount.as_view(), name='list_type_account'),
    url(r'^api/typerol/$', ListRol.as_view(), name='list_rol'),
    url(r'^api/typedoc/$', ListTypeDoc.as_view(), name='list_type_doc')
]