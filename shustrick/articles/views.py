from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest, Http404
from django.urls import reverse, reverse_lazy
from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'title': 'Index',
        'choosen_ref': 'articles:index',
        'objects': Article.objects.filter(is_published=True),
    }
    return render(request, "articles/index.html", context)


def detail(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    context = {
        'title': 'Detail',
        'object': obj,
        'choosen_ref': 'articles:detail',
        'comments': obj.comment_set.all(),
    }
    return render(request, "articles/detail.html", context)


@login_required(login_url=reverse_lazy("users:login"))
def create(request: HttpRequest):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.save()
            return HttpResponseRedirect(reverse_lazy('articles:index'))
        raise Http404("error")
    context = {
        'title': 'Create page',
        'form': ArticleForm(),
        'choosen_ref': 'articles:create',
    }
    return render(request, "articles/create.html", context)


@login_required(login_url=reverse_lazy("users:login"))
def add_comment(request):
    if request.method != "POST":
        raise Http404()
    data = request.POST.get('data')
    article_pk = request.POST.get('article_pk')
    article = get_object_or_404(Article, pk=article_pk)
    comment = Comment(data=data, article=article, sender=request.user)
    comment.save()
    return HttpResponseRedirect(reverse("articles:detail", kwargs={'pk':article_pk}))
    

@login_required(login_url=reverse_lazy("users:login"))
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.creator:
        article.delete()
        return HttpResponseRedirect(reverse_lazy("users:detail", kwargs={'pk': request.user.pk}))
    raise Http404()
    return
        

@login_required(login_url=reverse_lazy("users:login"))
def set_status(request, article_pk, status):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.creator:
        print('yo wtf')
        print(status)
        if status == 'public':
            article.is_published = True
        if status == 'hide':
            article.is_published = False
        article.save()
        return HttpResponseRedirect(reverse_lazy("users:detail", kwargs={'pk': request.user.pk}))

    raise Http404()