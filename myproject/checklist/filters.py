from django.db import models
from django import forms
import django_filters
from django_filters import filters

from .models import Checklist


filters.LOOKUP_TYPES = [
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
]

class ChecklistFilter(django_filters.FilterSet):

    class Meta:
        model = Checklist
        fields = ['title', 'start_date', 'completed', 'description']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'lookup_expr': ('gte','lte'),
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