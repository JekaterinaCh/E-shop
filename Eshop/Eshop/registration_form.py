from django import forms
from django.contrib.auth.hashers import make_password
from .models import User


class RegistrationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = User.objects.create(
            email=self.cleaned_data["email"],
            password=make_password(self.cleaned_data["password"])
        )
        if commit:
            user.save()
        return user
