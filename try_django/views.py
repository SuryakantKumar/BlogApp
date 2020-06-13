from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    context = {"title": 'Home Page'}
    if request.user.is_authenticated:
        context = {"title": 'Home Page', "user_content": [
            'profile', 'login', 'content']}
    return render(request, "home.html", context)


def about_page(request):
    context = {"title": 'About Us'}
    return render(request, "about.html", context)


def contact_page(request):
    context = {"title": 'Contact Us'}
    return render(request, "contact.html", context)


def example_page(request):
    title = 'Example'
    context = {"title": title}
    template_name = "title.txt"
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return render(request, "example.html", {"title": rendered_string})
