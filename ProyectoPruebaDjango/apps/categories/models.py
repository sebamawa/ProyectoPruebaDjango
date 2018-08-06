from django.db import models
from django import forms

# Create your models here.

class Category(models.Model):
    #id = models.AutoField(primary_key=True) #Added by default, not required explicitly
    name = models.CharField(max_length=30)
    description = models.TextField()
    #objects = models.Manager() #Added by default, not required explicitly

    def __str__(self):
        return "Name: %s - Category: %s" % (self.name, self.description)



# form para el modelo Category
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        # atributos secundarios
        labels = {
            'name': 'Nombre de la categoria:',
            'description': 'Descripción'
        }

        help_texts = {
            'name': 'Ingrese un nombre de categoria los mas descriptivo posible'
        }

        error_messages = {
            'name': {
                'max_length': "El nombre no puede tener mas de 30 caracateres"
            }
        }


      
