"""
MIT License
Copyright (c) 2017 Mackenzie Wangenstein, Chitradevi Maruthavanan, Andy Mayer


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Service
from .models import Organization
from .models import Testimony


# Create your views here.
def index(request):
  return render(request, 'website/index.html')


def safetymap(request):
  return render(request, 'website/safetymap.html')


def communityboard(request):
  return render(request, 'website/communityboard.html')


def testimonials(request):
    context = RequestContext(request)
    #get list of 10 testimonials and place in dict that gets displayed by template
    testimonials_list = Testimony.objects.order_by('title')[:10]
    context_dict = {'testimonials': testimonials_list}
    #Render response and send it back
    return render_to_response('website/testimonials.html', context_dict, context)


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
