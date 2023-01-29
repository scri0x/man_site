from django import forms
from django.core.exceptions import ValidationError
from man.models import Man, Category


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): # replace ----- -> Категория не выбрана
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Man
        fields = ['title', 'slug', 'content', 'photo', 'published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'some-input'}),
            'content': forms.Textarea(attrs={'rows': '20', 'cols': '60'}) ,
        }


    def clean_title(self): # title validation
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина заголовка привышает 200 символов')
        return title
