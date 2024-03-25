from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return HttpResponse("login")
    
def logout(request):
    return HttpResponse("logout")

    
def register(request):
    return HttpResponse("register")    