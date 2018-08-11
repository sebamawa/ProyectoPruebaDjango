from django.contrib import admin
from ProyectoPruebaDjango.apps.posts.models import Post

# Register your models here.

#admin.site.register(Post) #registra modelo en el admin

@admin.register(Post) #este decorador tambien registra el modelo en el admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') #permite visualizar campos en la lista de posts en el admin
