from django import forms
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r"^[0-9a-zA-Z_]*$", 'Разрешены только английские буквы и цифры.')

class OTPForm(forms.Form):
    password = forms.CharField(max_length=10, min_length=3, validators=[alphanumeric])
