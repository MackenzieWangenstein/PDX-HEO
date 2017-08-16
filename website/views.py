from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Service
from .models import Organization


# Create your views here.
def index(request):
  return render(request, 'website/index.html')


def safetymap(request):
  return render(request, 'website/safetymap.html')


def communityboard(request):
  return render(request, 'website/communityboard.html')


def testimonies(request):
  return render(request, 'website/testimonies.html')


def about(request):
  return render(request, 'website/about.html')


class OrganizationView(generic.DetailView):
  model = Organization
  template_name = 'website/organization.html'


class ServiceView(generic.DetailView):
  model = Service
  template_name = 'website/service.html'


def finder(request):
  service_list = Service.objects.order_by('name')
  service_paginator = Paginator(service_list, 10)
  organization_list = Organization.objects.order_by('name')
  organization_paginator = Paginator(organization_list, 10)
  page = request.GET.get('page')
  try:
    services = service_paginator.page(page)
    organizations = organization_paginator.page(page)
  except PageNotAnInteger:
    services = service_paginator.page(1)
    organizations = organization_paginator.page(1)
  except EmptyPage:
    services = service_paginator.page(service_paginator.num_pages)
    organizations = organization_paginator.page(organization_paginator.num_pages)
  return render(request, 'website/finder.html', {'page': page, 'services': services, 'organizations': organizations})
