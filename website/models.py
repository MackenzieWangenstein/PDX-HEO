from django.db import models


# Create your models here.
# Organizations provide services
class Organization(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  phone = models.CharField(max_length=200, blank=True, null=True)
  website = models.CharField(max_length=200, blank=True, null=True)
  email = models.CharField(max_length=200, blank=True, null=True)
  pub_date = models.DateTimeField('date published', auto_now_add=True)
  updated_date = models.DateTimeField('date updated', auto_now=True)
  hours_open = models.TimeField('open time', blank=True, null=True)
  hours_close = models.TimeField('close time', blank=True, null=True)

  def __str__(self):
    return self.name


class ServiceType(models.Model):
  name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published', auto_now_add=True)
  updated_date = models.DateTimeField('date updated', auto_now=True)

  def __str__(self):
    return self.name


class Service(models.Model):
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
  type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  phone = models.CharField(max_length=200, blank=True, null=True)
  website = models.CharField(max_length=200, blank=True, null=True)
  email = models.CharField(max_length=200, blank=True, null=True)
  updated_date = models.DateTimeField('date updated', auto_now=True)
  hours_open = models.TimeField('open time', blank=True, null=True)
  hours_close = models.TimeField('close time', blank=True, null=True)
  pub_date = models.DateTimeField('date published', auto_now_add=True)

  def __str__(self):
    return self.name
