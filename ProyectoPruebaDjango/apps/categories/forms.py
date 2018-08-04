from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(required=True, label='Ingrese el nombre de la categoría:')
    description = forms.CharField(widget=forms.Textarea)


