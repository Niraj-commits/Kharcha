import django_filters
from .models import *

class InfoFilter(django_filters.FilterSet):
    
    from_date = django_filters.DateFilter(field_name="created_at",lookup_expr="gte")
    to_date = django_filters.DateFilter(field_name="created_at",lookup_expr="lte")
    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains", label="Search")
    entry_type = django_filters.ChoiceFilter(choices=(('', 'All'), ('income', 'Income'), ('expense', 'Expense')), label='Type')
    
    class Meta:
        model = info
        fields = ['from_date','to_date','search','entry_type']

import django_filters
from .models import card

class CardFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Search")

    class Meta:
        model = card
        fields = ['search']
    