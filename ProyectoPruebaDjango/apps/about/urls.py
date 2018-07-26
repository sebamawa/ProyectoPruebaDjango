from django.urls import path
from ProyectoPruebaDjango.apps.about.views import contact, history

urlpatterns = [
    path('contact', contact),
    path('history', history)
]