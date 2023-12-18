from django import template
from news.models import Category

register = template.Library()


@register.inclusion_tag('news/cat_menu_tpl.html')
def show_cat_menu(cat_menu_class='cat_menu'):
    categories = Category.objects.all()
    return {"categories": categories, "cat_menu_class": cat_menu_class}
