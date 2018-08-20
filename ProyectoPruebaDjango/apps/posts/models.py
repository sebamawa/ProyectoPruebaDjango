from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    #We specify the name of the reverse relationship, from User to Post,
    #with the related_name attribute.This will allow us to access related objects easily.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',) #descending order by default when we query the database

    def __str__(self):
        return self.title

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

