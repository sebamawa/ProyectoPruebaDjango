from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ProyectoPruebaDjango.apps.entries.models import Entry, EntryModelForm

# CreateView (Class-based view)
class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryModelForm
    success_url = '/category/create' #reverse_lazy('entries:index')

def index (request):
    return HttpResponse('Index de Entries')

