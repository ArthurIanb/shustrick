from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "articles/index.html", {'title': 'Index'})


def detail(request, pk):
    return render(request, "articles/detail.html", {"title": "Detail", "object_pk": pk})



def create(request):
    return render(request, "articles/create.html", {"title": 'Create page'})

