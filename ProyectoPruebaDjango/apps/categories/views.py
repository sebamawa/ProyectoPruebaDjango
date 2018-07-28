from django.shortcuts import render
from django.http import HttpResponse
from ProyectoPruebaDjango.apps.categories.models import Category

# Create your views here.

#crea una categoria
def create(request):

    #create a model Category instance
    category = Category(name='Categoria 1', description='Categoria creada desde modelo')
    #invoke the save() method to create/save the record
    #NO record id reference, so a create operation is made and the reference is updated with id
    category.save()

    #change field on instance
    category.name = 'Categoria 2'

    print("Se creo la categoria con id = " + str(category.id))

    #invoke the save() method ti update/save record
    #record has id reference from prior save() call, so operation is update
    #category.save()
    category.save(update_fields=['name']) #actualiza solo el campo 'name'. Por defecto Django actualiza todos los campos

    print("Se actualizo la categoria con id = " + str(category.id))

    return HttpResponse('Categoria creada con exito') #imprime directamente en pagina

def search(request, category_id):

    try:
        category = Category.objects.get(id=category_id)
        return HttpResponse("Se cargo de la base de datos la categoria: %s" % category.name)
    except:
        return HttpResponse("No se encontro la categoria con id = %s" % category_id)