from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")


def detail(requst, pk):
    return HttpResponse(f"Checking article with pk {pk}")


def create(requst):
    return HttpResponse("Creating article")
