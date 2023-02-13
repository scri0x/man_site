from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import Man, Category


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # replace ----- -> Категория не выбрана
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Man
        fields = ['title', 'slug', 'content', 'photo', 'published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'some-input'}),
            'content': forms.Textarea(attrs={'rows': '20', 'cols': '60'}),
        }

    def clean_title(self):  # title validation
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина заголовка привышает 200 символов')
        return title


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Вопрос', widget=forms.Textarea(attrs={'cols': '60', 'rows': '10'}))
    captcha = CaptchaField(label='Капча')
