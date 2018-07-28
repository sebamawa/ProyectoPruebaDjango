from django.contrib import admin
from ProyectoPruebaDjango.apps.entries.models import Entry

# Register your models here.

#representa un modelo (Entry) en la interfaz admin. Se usa para customizar el modelo en el admin
class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Entry, EntryAdmin)
