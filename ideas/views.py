from msilib.schema import ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.models import User

from ideas.forms import LocalForm
from ideas.models import Local, Billing

def home(request):
    return render(request,'registration/home.html')

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


def local(request):
    if request.method == "POST":
        form = LocalForm(request.POST)
        if form.is_valid():
            local = Local(admin=request.user, owner=request.user, number=request.POST['number'], area=request.POST['area'])
            local.save()
        messages.success(request, f"Lokal został dodany")
    else:
        form = LocalForm()
    form = LocalForm()
    local = Local.objects.filter(admin=request.user)
    context = {
            'locals': local,
            'form': form,
    }
    return render(request, 'registration/local.html', context)