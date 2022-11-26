from django import forms
from . models import *

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['number', 'area', 'owner']