from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from apps.categoria.models import Categoria


def index(request):
    return HttpResponse("Index")

def categorias_list(request):
    categoria = Categoria.objets.all()
    context = {'categoras':categoria}
    return render(request, 'categorias_list.html', context)
