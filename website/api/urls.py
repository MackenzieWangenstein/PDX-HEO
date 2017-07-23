from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from . import views

urlpatterns = [
  url(r'^users/$', views.UserList.as_view()),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
  url(r'^organization/$', views.OrganizationList.as_view(), name='organization list'),
  url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationDetail.as_view(), name='organization'),
  url(r'^service/$', views.ServiceList.as_view(), name='service list'),
  url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view(), name='service'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
