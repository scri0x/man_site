from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from man.models import Man, Category
from man.forms import *
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
    template = 'man/addpage.html'
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # use form.save without try except
            return redirect('index')
    else:
        form = AddPostForm()

    context = {
        'title': 'Добавление статьи',
        'form': form,
    }
    return render(request, template, context)


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



def show_category(request, cat_slug):
    posts = Man.objects.filter(cat__slug=cat_slug)
    template = 'man/index.html'
 
    context = {
        'posts': posts,
        'title': 'Категория',
        'cat_selected': cat_slug,
    }
    return render(request, template, context)



def page_not_found(requst, exception):
    return HttpResponseNotFound("Страница не найдена")