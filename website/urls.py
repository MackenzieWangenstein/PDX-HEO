from django.conf.urls import url, include

from . import views
from . import testimonials_views
from django.conf import settings
#from django.conf import django.views

urlpatterns = [
  # ex: /pdxheo/
  url(r'^$', views.index, name='index'),
  url(r'^about/$', views.about, name='about'),
  url(r'^community/$', views.communityboard, name='community_board'),
  url(r'^finder/$', views.finder, name='finder'),
  url(r'^safety/$', views.safetymap, name='safety_map'),
  url(r'^testimonials/$', views.testimonials, name='testimonials'),
  url(r'^testimonials/(?P<pk>\d+)$', testimonials_views.TestimonyDetail.as_view(), name='testimonials_detail'),
  url(r'^testimonials/create', testimonials_views.TestimonyCreate.as_view(), name='testimony_create'),
  url(r'^testimonials/(?P<pk>\d+)/update/$', testimonials_views.TestimonyUpdate.as_view(), name='testimony_update'),
  url(r'^testimonials/(?P<pk>\d+)/delete/$', testimonials_views.TestimonyDelete.as_view(), name='testimony_delete'),
  url(r'^thanks', testimonials_views.get_thanks, name='thanks'),
  # ex: /pdxheo/organization/1/
  url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationView.as_view(), name='organization_detail'),
  # ex: /pdxheo/shelter/1/
  url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceView.as_view(), name='service_detail'),
  url(r'^api/', include('website.api.urls', namespace="api")),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
