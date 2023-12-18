from django import template
from news.models import Tag
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('news/tag_menu_tpl.html')
def show_tag_menu(tag_menu_class='tag_menu'):
    tags = Tag.objects.annotate(cnt=Count('news_cat')).filter(cnt__gt=0)
    return {"tags": tags, "tag_menu_class": tag_menu_class}
