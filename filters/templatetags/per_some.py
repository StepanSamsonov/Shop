from django import template
from product.models import *


register = template.Library()


@register.inclusion_tag('per_some_elems.html', takes_context=True)
def per_some_elems(context):
    filter_per_some = context['filter_per_some']
    items = PricePerSome.objects.all()
    res = ['За ' + elem.name for elem in items]
    return {'per_some_items': res, 'filter_per_some': filter_per_some}
