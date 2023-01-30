from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)


class Creatures(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')  # Для небольшого текста. Max_length = ограничение по длине текста
    content = models.TextField(blank=True, verbose_name='О существе')  # blank - это поле необязательно к заполнению
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото', blank=False)  # upload_to - куда мы загружаем файл, % буквы - год,месяц,день
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')  # Статья загружена, но не опубликована. Как черновик. True - запись по умолчанию публикауется
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')  # on_delete protect - нельзя удалить категорию, пока в ней есть записи. null - поле можно не заполнять

    def get_absolute_url(self):
        return reverse('view_articles', kwargs={"articles_id": self.pk})

    def __str__(self):  # для нормального отображения в админке
        return self.title

    class Meta:
        verbose_name = 'Cтатья'  # как будут называться записи в админке (ед. число), | мб изменить на Статью?
        verbose_name_plural = 'Статьи'  # как будут называться записи в админке (мн. число)
        ordering = ['title']  # - сортировка (c минусом будет в обратном порядке)


class Category(models.Model):  # - создание класса с категориями статей
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')  # db_index - индексирует поле

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'  # как будут называться категории в админке (ед. число)
        verbose_name_plural = 'Категории'  # как будут называться категории в админке (мн. число)
        ordering = ['title']  # - сортировка (c минусом будет в обратном порядке)


class Comments(models.Model):
    article = models.ForeignKey(Creatures, on_delete=models.CASCADE, verbose_name='Статья', blank=True, related_name='comments_creatures')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True)
    text_com = models.TextField(verbose_name='Текст комментария')

    def __str__(self):
        return str(self.article)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['author']


class Nichego(models.Model):
    title = models.CharField(max_length=150)
