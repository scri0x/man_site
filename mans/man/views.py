from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Man, Category
from .forms import *
from .templatetags.man_tags import *
from .utils import *


class ManIndex(DataMixin, ListView):
    model = Man
    template_name = "man/index.html"
    context_object_name = 'posts'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return Man.objects.filter(published=True).select_related('cat')


def about(request):
    template_name = 'man/about.html'
    cats = Category.objects.all()
    context = {
        'title': 'О нас',
        'menu': menu,
        'cats': cats,
    }
    return render(request, template_name, context)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'man/addpage.html'
    success_url = reverse_lazy('index')
    login_url = 'index'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание статьи')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('index')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'man/contact.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context | c_def


class ShowPost(DataMixin, DetailView):
    model = Man
    template_name = 'man/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])  # name of post in title
        return context | c_def


class ManCategory(DataMixin, ListView):
    model = Man
    template_name = 'man/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Man.objects.filter(cat__slug=self.kwargs['cat_slug'], published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return context | c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'man/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'man/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('index')


def user_logout(request):
    logout(request)
    return redirect('index')


def page_not_found(requst, exception):
    return HttpResponseNotFound("Страница не найдена")
