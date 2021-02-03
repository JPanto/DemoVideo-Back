from django.conf.urls import url
from Users.views import RegisterAPI, LoginAPI
from knox import views as knox_views


urlpatterns = [
    url(r'^api/register/$', RegisterAPI.as_view(), name='register'),
    url(r'^api/login/$', LoginAPI.as_view(), name='login'),
    url(r'^api/logout/$', knox_views.LogoutView.as_view(), name='logout'),
    url(r'^api/logoutall/$', knox_views.LogoutAllView.as_view(), name='logoutall'),
]