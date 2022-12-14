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
        fields = ['owner', 'value','addressee_name', 'bank_account', 'status', 'start_billing', 'end_billing', 'payment_date', 'details']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class FileUploadForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    file_data = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

class FileUploadForm2(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['file_name', 'my_file']