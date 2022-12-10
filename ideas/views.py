import datetime
from msilib.schema import ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.models import User

from ideas.forms import LocalForm, BillingForm, UserRegistrationForm, UserEditForm
from ideas.models import Local, Billing
from ideas.notification import send_notification


def home(request):

    locals = Local.objects.all()
    logged = 'nobody'
    for local in locals:
        if local.admin == request.user:
            logged = 'admin'
            break
        elif local.owner == request.user:
            logged = 'resident'
            break

    context = {'logged': logged,}
    return render(request,'registration/home.html', context)

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
            local = Local(
                admin=request.user,
                owner=User.objects.get(id=request.POST["owner"]),
                number=request.POST['number'],
                area=request.POST['area']
            )
            local.save()
            messages.success(request, f"Lokal został dodany")
    else:
        form = LocalForm()
    local = Local.objects.filter(admin=request.user)
    context = {
            'locals': local,
            'form': form,
    }
    return render(request, 'registration/local.html', context)

def local_delete(request, pk=None):
    Local.objects.get(id=pk).delete()
    return redirect("local")

def billing(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            try:
                paid = request.POST['status']
                if paid == 'on':
                    paid = True
                else:
                    paid = False
            except:
                paid = False
            billing = Billing(
                admin=request.user,
                owner=Local.objects.get(id=request.POST["owner"]),
                value=request.POST['value'],
                status=paid,
                start_billing=request.POST['start_billing'],
                end_billing=request.POST['end_billing'],
                payment_date=request.POST['payment_date'],
            )
            billing.save()
            messages.success(request, f"Rachunek został dodany")
    else:
        form = BillingForm()
    billing = Billing.objects.filter(status=False).filter(admin=request.user)
    context = {
        'billings': billing,
        'form': form,
    }
    return render(request, 'registration/billing.html', context)

def billing_history(request):
    billing = Billing.objects.filter(status=True).filter(admin=request.user)
    context = {
        'billings': billing,
    }
    return render(request, 'registration/billing_history.html', context)


def billing_update(request, pk=None):
    billing = Billing.objects.get(id=pk)
    if billing.status == True:
        billing.status = False
    else:
        billing.status = True
    billing.save()
    return redirect('billing')

def resident(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dodano nowego mieszkańca")
    else :
        form= UserRegistrationForm()
    resident = User.objects.all()
    context = {
        'residents' : resident,
        'form' : form,
    }
    return render(request, 'registration/resident.html', context)

def resident_billing(request):
    local = Local.objects.get(owner = request.user)
    billing = Billing.objects.filter(owner = local.id).filter(status=False)
    context = {
        'billings' : billing,
    }
    return render(request, 'registration/resident_billing.html', context)

def resident_billing_history(request):
    local = Local.objects.get(owner=request.user)
    billing = Billing.objects.filter(owner=local.id).filter(status=True)
    context = {
        'billings': billing,
    }
    return render(request, 'registration/resident_billing.html', context)

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
    return render(request, 'registration/edit_user.html', context)

# def administrator(request):
#     local = Local.objects.filter(owner = request.user)
#     administrator = User.objects.get(id=local.admin)
#     context = {
#         'administrator': administrator,
#     }
#     return(request, 'registration/admin_profile.html', context)

# def send():
#     billings = Billing.objects.filter(status = False)
#     now = datetime.date.today()
#     now = now.strftime('%d %m %Y')
#     now = datetime.strptime(now, '%d %m %Y')
#     nowDay = now.strftime('%d')
#     nowMonth = now.strftime('%m')
#     nowYear = now.strftime('%Y')
#     for element in billings:
#         time = element.payment_date
#         time = time.strftime('%d %m %Y')
#         time = datetime.strptime(time, '%d %m %Y')
#         timeMonth = time.strftime('%m')
#         timeYear = time.strftime('%Y')
#         #if nowMonth == timeMonth and nowYear == timeYear:
#             #dif = timeDay - nowDay
#         diff = abs((datetime.date(time[0],time[1],time[2]) - datetime.date(now[0],now[1],now[2])).days)
#         print(diff)


