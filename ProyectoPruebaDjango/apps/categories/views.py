from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse

from ProyectoPruebaDjango.apps.categories.forms import CategoryForm
from ProyectoPruebaDjango.apps.categories.models import Category, CategoryModelForm

# Create your views here.

#ejemplo de uso de save() - Para crear o actualizar categoria
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
    #record has id reference from prior save() call, so operation is update.
    #category.save()
    category.save(update_fields=['name']) #actualiza solo el campo 'name'. Por defecto Django actualiza todos los campos

    print("Se actualizo la categoria con id = " + str(category.id))

    return HttpResponse('Categoria creada con exito') #imprime directamente en pagina

#ejemplo de uso de get() para recuperar UN SOLO registro de categoria
def search(request, category_id):

    try:
        category = Category.objects.get(id=category_id)
        #category = Category.objects.get(name__contains='PHP') #error si get() recupera mas de un registro
        # category, createdOK = Category.objects.get_or_create(name="PHP") #si no recupera, crea un registro
                                                                        #usa get y save combinados
        return HttpResponse("Se cargo de la base de datos la categoria: %s" % category.name)
    except ObjectDoesNotExist:
        return HttpResponse("No se encontro la categoria con id = %s" % category_id)

    #prueba con input(). La pagina queda cargando hasta recibir el input
    # try:
    #     id_input = input("Ingrese el id de la categoria a buscar: ")
    #     category = Category.objects.get(id=int(id_input))
    #     return HttpResponse("Se cargo de la base de datos la categoria: %s" % category.name)
    # except:
    #    return HttpResponse("No se encontro la categoria con id = %s" % id_input)

#ejempl de uso de update()
def update(request, category_id):
    cant = Category.objects.filter(id=category_id).update(name='Programacion general') #si no se filtrara por primay key
    # (o campo unique), se podrian recuperar varios registros y update() los actualizaria a TODOS
    # filter() retorna un query set (se ve uso en la siguiente view (funcion index))
    return HttpResponse("Se actualizo el nombre de: %d categoria/s" % cant)

# ejemplo de uso de all(), filter() y in_builk() - para listar todas las categirias
def index(request):
    categories = Category.objects.all()
    #categories = Category.objects.filter(name='PHP') #recupero categorias con filtro (SELECT ... WHERE name = "PHP")
    #categories = Category.objects.in_bulk() #retorna un diccionario con los registros, no un queryset
    #print(categories.query) #permite ver la consulta SQL
    #Artificio: obtiene una lista de categorias (diccionarios) a partir del queryset de all() o filter()
    # Esto se hace para imprimir con el HttpResponse()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return HttpResponse(str(data))

# views para trabajar con formularios 

# create
def create_form(request):
    # crear categoria con model form (la clase del form se guarda en models.py junto al modelo)
    if request.method == 'POST':
        # POST, generate form with data from request
        form = CategoryModelForm(request.POST) #se instancia el form con los datos enviados por el
                            # usuario por si se debe reenviar al mismo con los datos por no ser validado
        # check if it's valid
        if form.is_valid():
            # Insert into DB
            form.save()
            # redirect to a new URL
            return HttpResponse('Categoria almacenada correctamente en la BD')
    else:
        # GET, generate unbound (blank) form
        form = CategoryModelForm()
    return render(request, 'categories/create.html', {'form':form})

# crear categoria con form standalone (independiente). La clase del form usada se guada en forms.py
"""     if request.method == "POST":
        # POST, generate form with data from request
        form = CategoryForm(request.POST)
        if form.is_valid:
            # process data, insert into DB, generate email, etc

            # redirect to a new URL
            return HttpResponse("Categoria agregada correctamente")

    else:
        # GET, generate blank form
        form = CategoryForm(initial={'description':'Descripcion opcional'})    
    return render(request, 'categories/create.html', {'form':form}) """