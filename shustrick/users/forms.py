from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    
    
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='login', widget=forms.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())
    
    class Meta:
        model = get_user_model()
        fields = ["username", "password", "confirm_password", "first_name", "last_name", "email"]
        
    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError("Passwords doesnt match")
        return cd["password"]
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email exists")
        return email