from ideas.functions.notification import deltaTime
from ideas.models import Local, Billing


def billing_list(request, status):
    local = Local.objects.get(owner=request.user)
    billing = Billing.objects.filter(owner=local.id).filter(status=status)
    return billing


def deadlineAproaching(request, billing):
    billing_deadline = []
    for bill in billing:
        if deltaTime(bill.payment_date) < 5 and deltaTime(bill.payment_date) >= 0:
            billing_deadline.append(bill)
    return billing_deadline


def unpaidBill(request, billing):
    unpaid = []
    for bill in billing:
        if deltaTime(bill.payment_date) < 0:
            unpaid.append(bill)
    return unpaid
