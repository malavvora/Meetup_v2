from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = 'meetup'
urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'^register/$', views.RegisterPage.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^(?P<pk>[0-9]+)/$', views.GroupView.as_view(), name='group'),
    url(r'^create-meetup/$', views.CreateMeetup.as_view(), name='create_meetup'),
    url(r'^profile/$', views.UserProfileView.as_view(), name='profile'),
    url(r'^group-details/(?P<pk>[0-9]+)$', views.GroupDetails.as_view(), name='group_details'),
]
