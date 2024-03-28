from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

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


@login_required(login_url=reverse_lazy("users:login"))
def detail(request, pk):
    if request.user.pk == pk:
        full_page = True
    else:
        full_page = False
    
    user = User.objects.get(pk=pk)
    articles = user.article_set.all()
    context = {
        'title': request.user.username,
        'articles': articles,
        'target_user': user,
        'full_page': full_page
    }
    return render(request, 'users/detail.html', context)