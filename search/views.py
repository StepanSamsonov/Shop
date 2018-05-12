from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from product.models import Product
from search.forms import SearchForm


@csrf_exempt
def search(request):
    text_search = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text_search = form.cleaned_data['text_search']
    else:
        form = SearchForm()

    searched = []

    return render(request, 'search.html', {'form': form}, locals())


    # kekos = Product.objects.all()
    # searched = []
    #
    # for product in products:
    #     if (text_search in product.name or text_search in product.description or text_search in product.characteristic
    #        or text_search in product.category.name or text_search in product.price_per_some.name
    #        or text_search in str(product.price)):
    #         searched.append(product)
    # len_prods = len(searched)