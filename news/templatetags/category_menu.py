from django import template
from news.models import Category

register = template.Library()


@register.inclusion_tag('news/category_menu_tpl.html')
def show_category_menu(category_menu_class='category_menu'):
    categories = Category.objects.all()
    return {"categories": categories, "category_menu_class": category_menu_class}
