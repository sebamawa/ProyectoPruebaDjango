from django.db import models
from ProyectoPruebaDjango.apps.categories.models import Category

# Create your models here.

class Entry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #crea relacion 1-N (1 categoria - N entradas)
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)