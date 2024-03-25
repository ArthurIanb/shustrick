from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest, Http404
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm


def index(request):
    context = {
        'title': 'Index',
        'objects': Article.objects.filter(is_published=True),
    }
    return render(request, "articles/index.html", context)


def detail(request, pk):
    context = {
        'title': 'Detail',
        'object': get_object_or_404(Article, pk=pk),
    }
    return render(request, "articles/detail.html", context)



def create(request: HttpRequest):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('articles:index'))
        raise Http404("error")
    context = {
        'title': 'Create page',
        'form': ArticleForm(),
    }
    return render(request, "articles/create.html", context)

