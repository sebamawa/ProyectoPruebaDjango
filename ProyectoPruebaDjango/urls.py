"""ProyectoPruebaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from ProyectoPruebaDjango.apps.about import views as about_views
from ProyectoPruebaDjango.apps.categories import views as categories_views
#from about_views import AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',TemplateView.as_view(template_name='homepage.html')), #redirge dirctamente a view html (class-based view basica para mostrar un template)
    path('about2/', about_views.AboutView.as_view()),

    path('about/', about_views.contact), #llama metodo 'contact' de controlador (views) de app 'about'
    path('about_all/', include('ProyectoPruebaDjango.apps.about.urls')), #otra forma a lo anterior (importa archivo urls de app 'about')

    #urls para pruebas CRUD con el modelo Category (app categories). Seria mas 'prolijo' poner
    #todas estas operaciones en el archivo urls.py de la app categories y hacer un include() como arriba con la app about
    path('category/create', categories_views.create),
    path('category/search/<int:category_id>/', categories_views.search), #'search_category/', categories_views.search)
    path('category/update/<int:category_id>/', categories_views.update),
    path('category/index', categories_views.index),

    #paths para trabajar con formularios de categorias
    path('category/create_form', categories_views.create_form)
]
