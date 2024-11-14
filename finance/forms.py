from django import forms
from django.core.exceptions import ValidationError
from .models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': "Email",
            'class': 'form-control'
        })
    )
    # phone_number = forms.CharField(
    #     max_length=15,
    #     min_length=10,
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         'placeholder': "Phone",
    #         'class': 'form-control'
    #     })
    # )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'placeholder': "Create a password",
            'class': 'form-control'
        })
        )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': "Confirm your password",
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('password do not match!')
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user
