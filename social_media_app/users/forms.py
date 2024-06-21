from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'display_picture', 'gender','Location']
        widgets = {
            'gender': forms.RadioSelect
        }