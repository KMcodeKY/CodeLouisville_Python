from django.db import models
from django import forms
import django_filters
from django_filters import filters

from .models import Checklist

filters.LOOKUP_TYPES = [
    ('lt', 'Less than'),
    ('gt', 'Greater than'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Less than or equal to'),
]

class ChecklistFilter(django_filters.FilterSet):

    class Meta:
        model = Checklist
        fields = ['title', 'description', 'category','start_date', 'end_date', 'completed']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'lookup_expr': ('gte','lte','gt','lt'),
                },
            },
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.RadioSelect(choices=[(True, 'Yes'),
                                                            (False, 'No'),("", 'Any')]),
                },
            },
        }