from django import forms
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z0-9_]{3,20}$",
                message="Username must contain 3–20 letters, numbers, or underscores.",
            )
        ],
        widget=forms.TextInput(attrs={
            "placeholder": "Enter username",
            "class": "input-field",
            "autocomplete": "username",
        }),
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Enter password",
            "class": "input-field",
            "autocomplete": "current-password",
        }),
    )
