# forms.py
from django import forms
from .models import Affiliate
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class AffiliateForm(forms.ModelForm):
    class Meta:
        model = Affiliate
        fields = ['title', 'price', 'discount', 'link', 'image', 'logo','old_price','color']
        
class AffiliateUpdate(forms.ModelForm):
    class Meta:
        model = Affiliate
        fields = ['title', 'price']


class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search Product', max_length=255, required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
