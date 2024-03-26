from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Login',
    }
    
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse_lazy("articles:index"))

    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return HttpResponseRedirect(reverse_lazy("users:login"))
    
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Registration',
        'form': form,
    }
    
    return render(request, 'users/register.html', context)