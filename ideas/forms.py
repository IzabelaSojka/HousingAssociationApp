from django import forms
from . models import *

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['number', 'area', 'owner']

class DateInput(forms.DateInput):
    input_type = 'date'

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        widgets = {'start_billing': DateInput(), 'end_billing': DateInput(), 'payment_date': DateInput()}
        fields = ['owner', 'value', 'status', 'start_billing', 'end_billing', 'payment_date']