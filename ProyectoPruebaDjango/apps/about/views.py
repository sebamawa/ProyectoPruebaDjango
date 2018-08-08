from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView


# Create your views here.
#metodo (funcion) de controlador (view basada en metodo)
def contact(request):
    # Content from request or database extracted here
    # and passed to the template for display

    #agrega mensaje flash
    messages.success(request, 'A llegado a la pagina de contacto!!!')
    
    return render(request, 'about/contact.html') #redirige a template de app
    #return HttpResponse('Prueba de impresion '+ request.META['REMOTE_ADDR']) #imprime directamente en pagina

def history(request):
    # create fixed data stuctures to pass to template
    # DATA COULD EQUALLY COME FROM DATABASE QUERIES,, WEB SERVICES OR SOCIAL API'S
    about_staff = {'gerente':'Sebastian Martinez', 'empleado':'Carlos Acosta'} #diccionario
    about_address = ['Gonzalo Ramirez 1723', 'Gonzalo Ramirez 1565'] #lista
    about_dates = ((0,''), (1,'3/1/1980')) #tupla   

    #diccionario para pasar a template
    values_for_template = {'about_staff':   about_staff,
                           'about_address': about_address,
                           'about_dates':   about_dates}

    #cuando se pasa el diccionario como ultimo argumento, este queda disponible en el template
    #para pasar datos a multiples templates se debe declarar un procesador de contexto
    return render(request, 'about/history.html', values_for_template)     


# Class-base view. Herencia de clases basadas en views
class AboutView(TemplateView):
    template_name = "about/contact.html"

