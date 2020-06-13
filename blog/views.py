from django.shortcuts import render
from .models import BlogPost


def blog_post_detail_page(request):
    obj = BlogPost.objects.get(id=1)
    context = {"title": 'blog ' + str(obj.id), "objects": obj}
    return render(request, "blog_post_detail.html", context)
