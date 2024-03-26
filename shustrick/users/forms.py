from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label='login', widget=forms.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())