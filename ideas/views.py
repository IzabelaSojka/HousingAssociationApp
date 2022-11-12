from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, CreateView

from ideas.models import Local


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

class RegisterPage(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

class LocalCreate(LoginRequiredMixin, CreateView):
    template_name = 'registration/local_create.html'
    model = Local
    fields = ['number', 'area', 'owner', 'first_name', 'last_name']

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super(LocalCreate, self).form_valid(form)

