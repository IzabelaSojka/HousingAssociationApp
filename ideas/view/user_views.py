from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import FormView

from ideas.forms import UserEditForm


class CustomLoginView(LoginView):
    template_name = 'registration/user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


class RegisterPage(FormView):
    template_name = 'registration/user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

@login_required
def editUser(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'registration/user/edit_user.html', context)