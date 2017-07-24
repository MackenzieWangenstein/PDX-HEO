from website.models import Organization, Service
from .serializers import OrganizationSerializer, ServiceSerializer
from rest_framework import generics


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
  """
    Create get,post, put, delete organization
  """
  queryset = Organization.objects.all()
  serializer_class = OrganizationSerializer


class OrganizationList(generics.ListCreateAPIView):

  """
  List all organizations or create a new organization
  """
  queryset = Organization.objects.all()
  serializer_class = OrganizationSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
      Create get,post, put, delete organization
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceList(generics.ListCreateAPIView):
    """
    List all organizations or create a new organization
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
