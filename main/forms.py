from django import forms
from django.core.validators import RegexValidator
from accounts.models import CustomUser

from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('title', 'description', 'photo')

class TourRegisterForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'nat_id', 'age', 'phone_number')