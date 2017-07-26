from django.conf.urls import url, include

from . import views
#from . import api.views.ServiceView


urlpatterns = [
  # ex: /pdxheo/
  url(r'^$', views.index, name='index'),
  url(r'^about/$', views.about, name='about'),
  url(r'^community/$', views.communityboard, name='community_board'),
  url(r'^finder/$', views.FinderView.as_view(), name='finder'),
  url(r'^safety/$', views.safetymap, name='safety_map'),
  url(r'^testimonies/$', views.testimonies, name='testimonies'),
  # ex: /pdxheo/organization/1/
  url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationView.as_view(), name='organization'),
  # ex: /pdxheo/shelter/1/
  #TODO - figure out how to make this view from the
  url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceView.as_view(), name='service'),
  url(r'^api/', include('website.api.urls', namespace="api")),
  #url(r'^api/service/)
  url(r'^service/$', views.ServiceView.as_view(), name='service'),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
