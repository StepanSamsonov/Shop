from django import template
from product.models import *


register = template.Library()


@register.inclusion_tag('categ_items.html', takes_context=True)
def categ_items(context):
    filter_categories = context['filter_categories']
    items = Category.objects.all()
    res = [elem.name for elem in items]
    return {'cat_items': res, 'filter_categories': filter_categories}
