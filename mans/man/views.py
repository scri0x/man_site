from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from man.models import Man, Category
from man.forms import *
from man.templatetags.man_tags import *
from man.utils import *


class ManIndex(DataMixin, ListView):
    model = Man
    template_name = "man/index.html"
    context_object_name = 'posts'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return Man.objects.filter(published=True)



def about(request):
    return render(request, 'man/about.html')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'man/addpage.html'
    success_url = reverse_lazy('index')
    login_url = 'index'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Создание статьи')
        return context | c_def


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Войти")


class ShowPost(DataMixin, DetailView):
    model = Man
    template_name = 'man/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post']) # name of post in title
        return context | c_def


class ManCategory(DataMixin, ListView):
    model = Man
    template_name = 'man/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Man.objects.filter(cat__slug=self.kwargs['cat_slug'], published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Категория - ' + str(context['posts'][0].cat), 
                                      cat_selected = context['posts'][0].cat_id)
        return context | c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name =  'man/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def 


def page_not_found(requst, exception):
    return HttpResponseNotFound("Страница не найдена")