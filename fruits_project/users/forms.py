from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


form_class = "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, label = 'Username', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter   Username'
        }
    ))
    email = forms.EmailField(max_length=100, label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        }
    ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        }
    ))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        }
    ))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Enter first name'
        }
    ))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Enter last name'
        }
    ))

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user