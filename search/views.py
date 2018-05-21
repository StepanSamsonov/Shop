from django.shortcuts import render
from product.models import Product, UserData
from search.forms import SearchForm, FilterForm
import sys


def search(request, filter_categories='Все'):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if not is_login:
        user_name = session_key
        try:
            UserData.objects.get(owner_name=user_name)
        except:
            UserData.objects.create(owner_name=user_name, liked_data='', order_data='')

    text_search = ''
    filter_price_from = 0
    filter_price_to = 10**6
    filter_per_some = 'Все'
    filter_is_exist = 'Все'
    filter_sort_by = 'filterRadioDown'

    if request.method == 'POST':
        if 'search_butt' in request.POST:
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                text_search = search_form.cleaned_data['text_search']
            filter_form = FilterForm()
        elif 'filter_butt' in request.POST:
            filter_form = FilterForm(request.POST)
            filter_form.fields['filter_sort_by'].label = 'filterRadioDown'
            if filter_form.is_valid():
                filter_sort_by = request.POST.get('filterRadio')
                filter_per_some = request.POST.get('filter_per_some')
                filter_price_from = filter_form.cleaned_data['filter_price_from']
                filter_price_to = filter_form.cleaned_data['filter_price_to']
                filter_is_exist = request.POST.get('filter_is_exist')
                filter_categories = request.POST.get('filter_categories')
                text_search = filter_form.cleaned_data['text_search']
            search_form = SearchForm()
    else:
        search_form = SearchForm()
        filter_form = FilterForm()

    products = Product.objects.all()
    searched = []
    for product in products:
        if (text_search in product.name or text_search in product.description or text_search in product.characteristic
           or text_search in product.category.name or text_search in product.price_per_some.name
           or text_search in str(product.price)):
            if filter_price_from <= product.price <= filter_price_to:
                if product.price_per_some.name == filter_per_some[3:] or filter_per_some == 'Все':
                    if ((product.is_active and filter_is_exist == 'Есть')
                       or (not product.is_active and filter_is_exist == 'Нет') or (filter_is_exist == 'Все')):
                        if product.category.name == filter_categories or filter_categories == 'Все':
                            searched.append(product)

    searched.sort(key=lambda elem: elem.price, reverse=(filter_sort_by == 'filterRadioDown'))
    len_prods = len(searched)
    return render(request, 'search.html', locals())
