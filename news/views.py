from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F
from .models import *


class Home(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context


class NewsByCategory(ListView):
    template_name = 'news/category.html'
    context_object_name = 'news'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category__slug=self.kwargs['slug']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetNews(DetailView):
    model = News
    template_name = 'news/single.html'
    context_object_name = 'new'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class NewsByTags(ListView):
    template_name = 'news/category.html'
    context_object_name = 'news'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(tags__slug=self.kwargs['slug']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class Search(ListView):
    template_name = 'news/search.html'
    context_object_name = 'news'
    paginate_by = 6

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&"
        return context
