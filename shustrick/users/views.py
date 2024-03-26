from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Login',
    }
    
@login_required
def logout_user(request):
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


@login_required
def detail(request, pk):
    if request.user.pk != pk:
        return HttpResponse("You have no permissions for this page")
    
    articles = request.user.article_set.all()
    context = {
        'title': request.user.username,
        'articles': articles,
    }
    return render(request, 'users/detail.html', context)