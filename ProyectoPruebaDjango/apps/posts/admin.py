from django.contrib import admin
from ProyectoPruebaDjango.apps.posts.models import Post

# Register your models here.

#admin.site.register(Post) #registra modelo en el admin

@admin.register(Post) #este decorador tambien registra el modelo en el admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') #permite visualizar campos en la lista de posts en el admin

    list_filter = ('status', 'created', 'publish', 'author') #genera panel derecho con filtros (en lista de posts)

    search_fields = ('title', 'body') #genera campo de busqueda para filtrar

    prepopulated_fields = {'slug':('title',)} #rellena campo slug segun lo escrito en campo title (en form de insert)

    raw_id_fields = ('author',) #agrega lupa para ver lista de autores en popup (no en select), en form de insert

    ordering = ('status', 'publish')
