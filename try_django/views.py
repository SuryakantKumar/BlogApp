from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    return render(request, "home.html", {"title": 'Home Page'})


def about_page(request):
    return render(request, "about.html", {"title": 'About Us'})


def contact_page(request):
    return render(request, "contact.html", {"title": 'Contact Us'})


def example_page(request):
    title = 'Example'
    context = {"title": title}
    template_name = "title.txt"
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return render(request, "example.html", {"title": rendered_string})
