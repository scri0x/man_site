from django import template
from man.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('man/list_link_menu.html')
def show_menu_items():
    menu = [{'title': 'О сайте',
            'url_name':'about'},

            {'title': 'Добавить статью',
            'url_name':'addpage'},

            {'title': 'Обратная связь',
            'url_name':'contact'},
            
            {'title': 'Войти', 
            'url_name':'login'},
    ]
    return {'menu': menu}


# @register.inclusion_tag('man/list_categories.html')
# def show_categories():
#     cats = Category.objects.all()
#     return {'cats': cats}