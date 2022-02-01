from django import forms
from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth.forms import UserChangeForm

# Create your views here.

class Login(View):

    def get(self, request):
        form=UserChangeForm()
        return render(request, 'login.html', {'form':form})
        

    def post(self, request):
        pass