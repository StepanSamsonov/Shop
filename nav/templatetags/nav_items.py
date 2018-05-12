from django import template
from product.models import *


register = template.Library()


@register.inclusion_tag('dropdown.html', takes_context=True)
def dropdown(context):
    res = []
    for elem in Category.objects.all():
        url = '_'.join(elem.name.split(' '))
        res.append([elem.name, url])
    return {'items': res}
