from django.db import models
from django.urls import reverse
from django.conf import settings

DEFAULT_IMAGE_1 = "/static/website/Default_img.png"
class Testimony(models.Model):
    title = models.CharField(max_length=150)
    creator = models.ForeignKey('auth.User', related_name='testimonials', on_delete=models.CASCADE, blank=True, null=True)
    story = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='documents', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('testimonials_detail', kwargs={'pk': self.pk})

    def getImage(self):
        if not self.image:
            return DEFAULT_IMAGE_1

    class Meta:
        verbose_name_plural = "testimonials"



# Create your models here.
# Organizations provide services
class Organization(models.Model):
  name = models.CharField(max_length=200)
  creator = models.ForeignKey('auth.User', related_name='organizations', on_delete=models.CASCADE, blank=True, null=True)
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
  creator = models.ForeignKey('auth.User', related_name='services', on_delete=models.CASCADE, blank=True, null=True)
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

  def get_absolute_url(self):
    return reverse('service_detail', args=[self.pk])
