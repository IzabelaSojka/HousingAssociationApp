from django.shortcuts import render

from ideas.functions.billing_function import billing_list, unpaidBill, deadlineAproaching
from ideas.functions.user_function import whoLogged


def home(request):
    logged = whoLogged(request)
    billing_deadline = []
    unpaid = []
    if logged == 'resident':
        billing = billing_list(request, False)
        billing_deadline = deadlineAproaching(request, billing)
        unpaid = unpaidBill(request, billing)

    context = {
        'logged': logged,
        'billing_deadline': billing_deadline,
        'unpaid': unpaid,
    }
    return render(request, 'registration/home.html', context)













