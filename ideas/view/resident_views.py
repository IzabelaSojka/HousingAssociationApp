from django.contrib.auth.models import User
from django.shortcuts import render

from ideas.forms import UserRegistrationForm
from django.contrib import messages

from ideas.models import Local, Billing


def resident(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dodano nowego mieszkańca")
    else:
        form = UserRegistrationForm()
    resident = User.objects.all()
    context = {
        'residents': resident,
        'form': form,
    }
    return render(request, 'registration/resident/resident.html', context)


def resident_detail(request, pk=None):
    resident = User.objects.get(id=pk)
    local = Local.objects.get(owner=pk)
    context = {
        'resident': resident,
        'local': local,
    }
    return render(request, 'registration/resident/resident_detail.html', context)

def resident_billings(request, pk=None):
    local = Local.objects.get(owner=pk)
    billing = Billing.objects.filter(owner=local.id).order_by('-payment_date')
    context = {
        'billing': billing,
    }
    return render(request, 'registration/resident/resident_billing_all.html', context)