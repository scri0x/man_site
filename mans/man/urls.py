from django.urls import path
from man.views import *

urlpatterns = [
    path('', ManIndex.as_view(), name='index'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ManCategory.as_view(), name="category"),
]
