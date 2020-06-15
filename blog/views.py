from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# get  --> returns 1 value
# filter  --> returns [] of values so we can apply index also on filter


def blog_post_list_view(request):
    # List out objects
    # could be search
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # Create object
    # ? Use a form
    template_name = 'blog/create.html'
    context = {"form": None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object --> Detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/update.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    context = {"object": obj}
    return render(request, template_name, context)
