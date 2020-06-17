from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {"title": 'Home Page',
               'blog_list': qs}
    # if request.user.is_authenticated:
    #     context = {"title": 'Home Page', "user_content": [
    #         'profile', 'login', 'content']}
    return render(request, "home.html", context)


def about_page(request):
    context = {"title": 'About Us'}
    return render(request, "about.html", context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": 'Contact Us',
               "form": form}
    return render(request, "contact_form.html", context)


def example_page(request):
    title = 'Example'
    context = {"title": title}
    template_name = "title.txt"
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return render(request, "example.html", {"title": rendered_string})
