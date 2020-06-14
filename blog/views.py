from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# get  --> returns 1 value
# filter  --> returns [] of values so we can apply index also on filter


def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"title": obj.title, "objects": obj}
    return render(request, "blog_post_detail.html", context)
