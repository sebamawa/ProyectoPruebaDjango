from django.shortcuts import render
from django.http import HttpResponse
from ProyectoPruebaDjango.apps.categories.models import Category

# Create your views here.

#crea una categoria
def create(request):

    category = Category(name='Categoria 2 creada desde modelo', description='Descripcion de la categoria')
    category.save()

    return HttpResponse('Categoria creada con exito') #imprime directamente en pagina
