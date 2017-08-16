from website.models import Organization, Service, Testimony
from .serializers import OrganizationSerializer, ServiceSerializer, UserSerializer, TestimonySerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy

from django.contrib.auth.models import User #TODO - change to user in project when re-introduced
import views

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'services': reverse_lazy('api:service-list', request=request, format=format),
        'organizations': reverse_lazy('api:organization-list', request=request, format=format),
        'testimonials': reverse_lazy('api:testimonials_list', request=request, format=format)
    })



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  queryset = Organization.objects.all()
  serializer_class = OrganizationSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

  def perform_create(self, serializer):
      serializer.save(creator=self.request.user)

class TestimonyViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  queryset = Testimony.objects.all()
  serializer_class = TestimonySerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

  def perform_create(self, serializer):
      serializer.save(creator=self.request.user)



class ServiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TestimonyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
