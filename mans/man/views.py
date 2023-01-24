from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from man.models import Man, Category
from man.templatetags.man_tags import *


def index(request):
    posts = Man.objects.all()
    template = 'man/index.html'

    context = {
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, template, context)


def about(request):
    return render(request, 'man/about.html')



def addpage(request):
    return HttpResponse("Добавить статью")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Войти")


def show_post(request, post_slug):
    post = get_object_or_404(Man, slug=post_slug)
    template = 'man/post.html'

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, template, context)



def show_category(request, cat_id):
    posts = Man.objects.filter(cat_id=cat_id)
    template = 'man/index.html'
 
    context = {
        'posts': posts,
        'title': 'Категория',
        'cat_selected': cat_id,
    }
    return render(request, template, context)



def page_not_found(requst, exception):
    return HttpResponseNotFound("Страница не найдена")