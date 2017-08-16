from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from . import views

service_list = views.ServiceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

service_detail = views.ServiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'

})
#
organization_list = views.OrganizationViewSet.as_view({
'get': 'list',
'post': 'create'
})

organization_detail = views.OrganizationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'

})

user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})



urlpatterns = [
  url(r'^$', views.api_root),
  url(r'^users/$', user_list, name='user-list'),
  url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user'),
  url(r'^organization/$', organization_list, name='organization-list'),
  url(r'^organization/(?P<pk>[0-9]+)/$', organization_detail, name='organization'),
  url(r'^service/$', service_list, name='service-list'),
  url(r'^service/(?P<pk>[0-9]+)/$', service_detail, name='service'),
]

#
urlpatterns = format_suffix_patterns(urlpatterns)
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
