from django import forms
from django.forms import ModelForm
from .models import Testimony
from rest_framework import serializers

class TestimonyForm(ModelForm):
    def clean_title(self):
        data = self.cleaned_data['title']
        return data;

    def clean_story(self):
        data = self.cleaned_data['story']
        return data;

    def clean_author(self):
        data = self.cleaned_data['author']
        return data;

    def clean_image(self):
        data = self.cleaned_data['image']
        return data;

    class Meta:
        model = Testimony
        fields = ['title', 'story', 'author']



#creating a form to add a testimony
#form = TestimonyForm()

#creating a form to chang an existinng testimony
#testimony = Testimony.objects.get(pk=2)
# form = TestimonyForm(instance=testimony)

#class TestimonySerializer(FormSer)
