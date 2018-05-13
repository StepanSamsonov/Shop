import sys

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from search.forms import SearchForm


def search(request):
    text = request.session.get('text_search')
    print(sys.stderr, 'IN SEARCH')
    return render(request, 'search.html', locals())


    # kekos = Product.objects.all()
    # searched = []
    #
    # for product in products:
    #     if (text_search in product.name or text_search in product.description or text_search in product.characteristic
    #        or text_search in product.category.name or text_search in product.price_per_some.name
    #        or text_search in str(product.price)):
    #         searched.append(product)
    # len_prods = len(searched)