from django.db import models
from django.urls import reverse

"""
Category
--------
title, slug

Tag
--------
title, slug


News
--------
title, slug, author, content, created_at, photo, views, category, tag
"""


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-title']


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, verbose_name='url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='news_cat')
    tags = models.ManyToManyField(Tag, blank=True, related_name='news_cat')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
