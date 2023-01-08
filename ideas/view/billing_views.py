from django.shortcuts import render, redirect

from ideas.forms import BillingForm
from ideas.functions.billing_function import billing_list
from ideas.functions.user_function import whoLogged
from ideas.models import Billing, Local
from django.contrib import messages


def billing(request):
    if request.method == "POST":
        form = BillingForm(request.POST, request.FILES)
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
                addressee_name=request.POST['addressee_name'],
                bank_account=request.POST['bank_account'],
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
    return render(request, 'registration/billing/billing.html', context)


def billing_history(request):
    billing = Billing.objects.filter(status=True).filter(admin=request.user)
    context = {
        'billings': billing,
    }
    return render(request, 'registration/billing/billing_history.html', context)


def billing_update(request, pk=None):
    billing = Billing.objects.get(id=pk)
    if billing.status == True:
        billing.status = False
    else:
        billing.status = True
    billing.save()
    return redirect('billing')


def billing_detail(request, pk=None):
    billing = Billing.objects.get(id=pk)
    logged = whoLogged(request)
    context = {
        'billing': billing,
        'logged': logged,
    }
    return render(request, 'registration/billing/billing_detail.html', context)


def resident_billing(request):
    billing = billing_list(request, False)
    context = {
        'billings': billing,
    }
    return render(request, 'registration/billing/resident_billing.html', context)


def resident_billing_history(request):
    billing = billing_list(request, True)
    context = {
        'billings': billing,
    }
    return render(request, 'registration/billing/resident_billing.html', context)
