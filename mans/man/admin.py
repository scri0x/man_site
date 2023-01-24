from django.contrib import admin
from man.models import *

class ManAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'photo', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'time_create')
    prepopulated_fields = {'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Man, ManAdmin)
admin.site.register(Category, CategoryAdmin)


