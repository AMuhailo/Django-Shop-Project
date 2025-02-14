from django.shortcuts import get_object_or_404
from django import template
from shop.models import Category

register = template.Library()

@register.inclusion_tag('pages/include/categories.html')
def categories_list(category_slug, category_id):
    categories = Category.objects.all()
    if category_slug and category_id:
        category = get_object_or_404(Category,
                                     slug = category_slug,
                                     id = category_id)
    else:
        category = None
    context = {
        'categories':categories,
        'category':category
    }
    return context