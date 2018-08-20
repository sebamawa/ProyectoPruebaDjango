from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from ProyectoPruebaDjango.apps.entries.models import Entry, EntryModelForm

def index (request):
    return HttpResponse('Index de Entries')

# CreateView (Class-based view)
class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryModelForm
    success_url = '/create' #reverse_lazy('entries:index')

# ListView (Class-based view)
class EntryListView(ListView):
    model = Entry

