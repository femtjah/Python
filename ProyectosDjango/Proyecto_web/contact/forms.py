from django import forms

class FormsContact(forms.Form):
    name=forms.CharField(label='Nombre',required=True)
    email=forms.EmailField(label='Email', required=True)
    content=forms.CharField(label='Contenido', widget=forms.Textarea)