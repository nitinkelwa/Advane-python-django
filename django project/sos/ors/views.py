from django.http import HttpResponse
from django.shortcuts import render


def text_ors(request):
    return HttpResponse("<h1>This is my ors app </h1>")

def welcome(request):
    return render(request, "welcome.html")

def login(request):
    return render(request,"login.html")

def registration (request):
    return render(request,"registration.html")