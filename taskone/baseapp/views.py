from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "baseapp/index.html")


def aboutus(request):
    return render(request, "baseapp/about.html")


def contactus(request):
    return render(request, "baseapp/contact.html")


def details(request):
    return render(request, "baseapp/details.html")


def helpful(request):
    return HttpResponse("<h1>Thank you for Django framework</h1>")
