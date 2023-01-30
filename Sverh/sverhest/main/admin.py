from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Creatures, Category, Comments


class CreaturesAdmin(admin.ModelAdmin):  # - для вывода в админку нужных полей БД

    list_display = ('id', 'title', 'category', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')  # - через какие поля можно просмотреть статью
    search_fields = ('title', 'content')  # - по каким полям можно осуществлять поиск
    list_editable = ('is_published',)
    list_filter = ('title', 'category', 'is_published')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published')
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="170">')

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):  # - для вывода категории в админку и нужных полей БД
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  # - через какие поля можно просмотреть статью
    search_fields = ('title',)  # - по каким полям можно осуществлять поиск


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('article', 'text_com', 'author',)
    list_display_links = ('article', 'text_com', 'author',)
    search_fields = ('text_com', 'author',)


admin.site.register(Creatures, CreaturesAdmin)  # важен порядок передачи аргументов, сначала регистрация модели
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)

# admin.site.site_title = 'Управление статьями'
