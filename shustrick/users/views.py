from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import login, logout, authenticate


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("articles:index"))
                
    else:
        form = UserLoginForm()
    context = {
        'title': 'login page',
        'form': form,
    }
    return render(request, 'users/login.html', context)
        
    
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse("articles:index"))

    
def register(request):
    return HttpResponse("register")    