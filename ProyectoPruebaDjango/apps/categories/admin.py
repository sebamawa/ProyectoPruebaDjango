from django.contrib import admin
from ProyectoPruebaDjango.apps.categories.models import Category


# Register your models here.

#representa un modelo (Category) en la interfaz admin. Se usa para customizar el modelo en el admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

#admin.site.register(Category)
admin.site.register(Category, CategoryAdmin) #con la clase CategoryAdmin permite ver el id de una Category en el admin
