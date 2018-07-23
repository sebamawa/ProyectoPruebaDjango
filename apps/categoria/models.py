from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    body = models.TextField(max_length=550)