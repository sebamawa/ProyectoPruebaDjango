from django.urls import path
# from ProyectoPruebaDjango.apps.entries.views import EntryCreateView, EntryListView
from .views import EntryCreateView, EntryListView

app_name = 'entries'
urlpatterns = [
    path('', EntryListView.as_view(), name='index'),
    path('create', EntryCreateView.as_view(), name='create') # class-based view
]