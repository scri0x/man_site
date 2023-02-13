from django.urls import path
from .views import *

urlpatterns = [
    path('', ManIndex.as_view(), name='index'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path("register/", RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ManCategory.as_view(), name="category"),
]
