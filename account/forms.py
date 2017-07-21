from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    repassword = forms.CharField(label='Comfirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_repassword(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repassword']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['repassword']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme', 'photo')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

