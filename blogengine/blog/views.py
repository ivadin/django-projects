# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse

from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from .models import Post, Tag
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all().order_by('-date_pub')
    return render(request, "blog/index.html", context={"posts": posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "blog/post_detail.html"

    def post(self, request, slug):
        obj = Post.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse("posts_list_url"))


def tags_list(request):
    if request.is_ajax():
        print("This is ajax", request.GET["slug"])
        obj = Tag.objects.get(slug__iexact=request.GET["slug"])
        obj.delete()
        return HttpResponse("Tag remove!")

    tags = Tag.objects.all()
    return render(request, "blog/tags_list.html", context={"tags": tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "blog/tag_detail.html"


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = "blog/tag_create.html"


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = "blog/post_create.html"


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'
