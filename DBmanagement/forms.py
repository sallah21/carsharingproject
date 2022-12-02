from django import forms
from .models import *
class BaseFrom(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
