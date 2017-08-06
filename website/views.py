from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import generic

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


class FinderView(generic.ListView):
  template_name = 'website/finder.html'
  context_object_name = 'service_list'

  def get_queryset(self):
    return Service.objects.order_by('name')[:10]


class OrganizationView(generic.DetailView):
  model = Organization
  template_name = 'website/organization.html'


class ServiceView(generic.DetailView):
  model = Service
  template_name = 'website/service.html'
