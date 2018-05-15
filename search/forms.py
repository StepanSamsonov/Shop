from django import forms
from product.models import *


class SearchForm(forms.Form):
    text_search = forms.CharField(max_length=100, required=False)


class FilterForm(forms.Form):
    choices_for_sort_by = [('filterRadioUp', 'filterRadioUp'), ('filterRadioDown', 'filterRadioDown')]
    choices_for_per_some = [('За ' + elem.name, 'За ' + elem.name) for elem in PricePerSome.objects.all()]
    choices_for_per_some.append(('Все', 'Все'))
    choices_for_exist = [('Все', 'Все'), ('Есть', 'Есть'), ('Нет', 'Нет')]
    choices_for_categories = [(elem.name, elem.name) for elem in Category.objects.all()]
    choices_for_categories.append(('Все', 'Все'))

    filter_sort_by = forms.ChoiceField(choices=choices_for_sort_by, widget=forms.RadioSelect(), required=False, initial='filterRadioDown')
    filter_price_from = forms.IntegerField(required=False)
    filter_price_to = forms.IntegerField(required=False)
    filter_per_some = forms.ChoiceField(choices=choices_for_per_some, required=False, initial='Все')
    filter_is_exist = forms.ChoiceField(choices=choices_for_exist, required=False, initial='Все')
    filter_categories = forms.ChoiceField(choices=choices_for_categories, required=False, initial='Все')
    text_search = forms.CharField(max_length=100, required=False)
