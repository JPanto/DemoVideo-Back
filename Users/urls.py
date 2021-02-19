from django.conf.urls import url

from Users.views import RegisterAPI, LoginAPI, ListTypeLogin, \
                        ListTypeAccount, ListRol, ListTypeDoc, \
                        AccountDetail
from knox import views as knox_views

urlpatterns = [
    url(r'^api/register/$', RegisterAPI.as_view(), name='register'),  # Post register / create a new account
                                                                      # Return: User object, token authentication
    url(r'^api/login/$', LoginAPI.as_view(), name='login'),  # Post login
                                                             # Return: token authentication, expiry
    url(r'^api/logout/$', knox_views.LogoutView.as_view(), name='logout'),  # Post Logout
                                                                            # delete token authentication
    url(r'^api/logoutall/$', knox_views.LogoutAllView.as_view(), name='logoutall'),  # Post Logoutall
                                                                                     # delete all tokens authentication
    url(r'^api/typelogin/$', ListTypeLogin.as_view(), name='list_type_login'),  # Get all login types list
    url(r'^api/typeaccount/$', ListTypeAccount.as_view(), name='list_type_account'),  # Get all account types list
    url(r'^api/typerol/$', ListRol.as_view(), name='list_rol'),  # Get all rol list
    url(r'^api/typedoc/$', ListTypeDoc.as_view(), name='list_type_doc'),  # Get all doc types list
    url(r'^api/account/(?P<pk>[0-9]+)$', AccountDetail.as_view(), name='account_detail'),   # Get a specific account data
]