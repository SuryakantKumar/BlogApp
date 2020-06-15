from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
