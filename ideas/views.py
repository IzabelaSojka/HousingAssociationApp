from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import FormView, DetailView
from .models import Administrator, Local

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True