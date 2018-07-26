from django.shortcuts import render

# Create your views here.

#metodo de controlador de la app about
def contact(request):
    # Content from request or database extracted here
    # and passed to the template for display
    return  render(request, 'about/contact.html') #render es un helper django (similar a view() en laravel)
