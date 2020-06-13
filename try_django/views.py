from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "home.html", {"title": 'Home Page'})


def about_page(request):
    return render(request, "about.html", {"title": 'About Us'})


def contact_page(request):
    return render(request, "contact.html", {"title": 'Contact Us'})
