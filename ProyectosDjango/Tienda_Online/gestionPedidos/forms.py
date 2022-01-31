from django import forms
from django.forms.forms import Form

class FormularioContacto(forms.Form):

    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()

