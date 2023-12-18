from django import template
from news.models import News, Tag
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('news/popular_news_right_tpl.html')
def get_popular_right(cnt=5):
    news = News.objects.order_by('-views')[:cnt].select_related()
    return {"news": news}


@register.inclusion_tag('news/popular_news_up_tpl.html')
def get_popular_up(cnt=8):
    news = News.objects.order_by('-views')[:cnt]
    return {"news": news}


@register.inclusion_tag('news/featured_tpl.html')
def get_featured(cnt=8):
    news = News.objects.order_by('-created_at')[:cnt]
    return {"news": news}