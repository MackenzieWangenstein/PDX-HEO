from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
  url(r'^organization/$', views.OrganizationList.as_view(), name='organization list'),
  url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationDetail.as_view(), name='organization'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
