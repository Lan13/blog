from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'mail']
        labels = {'avatar': '', 'bio': 'bio', 'mail': 'mail'}
