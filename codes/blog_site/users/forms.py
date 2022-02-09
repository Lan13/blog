from .models import Profile
from django import forms
from captcha.fields import CaptchaField


class ProfileForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'mail']
        labels = {'avatar': '', 'bio': 'bio', 'mail': 'mail'}


class CaptchaForm(forms.Form):
    captcha = CaptchaField()
