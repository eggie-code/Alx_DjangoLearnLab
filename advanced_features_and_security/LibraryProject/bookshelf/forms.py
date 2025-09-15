# bookshelf/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number')
        
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=False, label='Book Title')
    author = forms.CharField(max_length=100, required=False, label='Author Name')
    library = forms.CharField(max_length=100, required=False, label='Library Name')