from django import template
from django.db.models import Count, F

from main.models import Category, Creatures
# from sverhest.models import Category

register = template.Library()


# другой вид следующей записи (на 16 строке), а этот не используется
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('main/list_categories.html')
def show_categories(arg1='Категории:'):  # мб надо убрать аргументы
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('creatures', filter=F('creatures__is_published'))).order_by('title')  # подсчитывает только то, что опубликовано
    return {"categories": categories, "arg1": arg1}
