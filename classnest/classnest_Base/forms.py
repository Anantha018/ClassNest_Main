# classnest_Base/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'contact', 'links']

class PasswordResetForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm New Password")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")