from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

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

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']