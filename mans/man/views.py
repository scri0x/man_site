from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from man.models import Man, Category
from man.forms import *
from man.templatetags.man_tags import *


class ManIndex(ListView):
    model = Man
    template_name = "man/index.html"
    context_object_name = 'posts'
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Man.objects.filter(published=True)



def about(request):
    return render(request, 'man/about.html')


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'man/addpage.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Войти")


class ShowPost(DetailView):
    model = Man
    template_name = 'man/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'] # name of post in title
        return context


class ManCategory(ListView):
    model = Man
    template_name = 'man/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Man.objects.filter(cat__slug=self.kwargs['cat_slug'], published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


def page_not_found(requst, exception):
    return HttpResponseNotFound("Страница не найдена")