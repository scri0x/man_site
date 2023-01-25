from django.urls import path
from man.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name="category"),
]
