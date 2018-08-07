from django.urls import path
from ProyectoPruebaDjango.apps.entries.views import EntryCreateView

app_name = 'entries'
urlpatterns = [
    path('create', EntryCreateView.as_view(), name='create') # class-based view
]