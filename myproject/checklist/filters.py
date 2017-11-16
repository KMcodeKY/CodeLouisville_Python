from django.db import models
from django import forms
import django_filters
from django_filters import filters

from .models import Checklist

# Spell out lookup types for Filter view display
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
            #Character fields filter by 'contains'
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            #Text fields filter by 'contains'
            models.TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            # Date fields filter by less than, greater than, less than or equal to, and greater than or equal to
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'lookup_expr': ('gte','lte','gt','lt'),
                },
            },
            #Boolean fields filter by true, false, and any (all)
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.RadioSelect(choices=[(True, 'Yes'),
                                                            (False, 'No'),("", 'Any')]),
                },
            },
        }