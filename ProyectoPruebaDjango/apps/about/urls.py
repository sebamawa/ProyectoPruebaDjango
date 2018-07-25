from django.urls import path
from ProyectoPruebaDjango.apps.about.views import contact

urlpatterns = [
    path('', contact),
]