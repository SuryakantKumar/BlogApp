from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    title = 'Home Page'
    return render(request, "home.html", {"title": title})


def about_page(request):
    return HttpResponse("<h1>About Us</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact Us</h1>")
