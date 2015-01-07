# -*- coding: utf-8 -*-
import django_filters as filters
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django_tables2.utils import AttributeDict


class CustomCheckBoxColumn(tables.CheckBoxColumn):

    @property
    def header(self):
        default = {"type": "checkbox",
                   "class": "toggle-all",
                   }
        general = self.attrs.get('input')
        specific = self.attrs.get('th__input')
        attrs = AttributeDict(default, **(specific or general or {}))
        return mark_safe('<input %s /> ' % attrs.as_html())

    def render(self, value, bound_column):  # pylint: disable=W0221
        default = {
            'type': 'checkbox',
            'name': bound_column.name,
            'class': 'id-check',
            'value': value
        }
        general = self.attrs.get('input')
        specific = self.attrs.get('td__input')
        attrs = AttributeDict(default, **(specific or general or {}))
        return mark_safe('<input %s/>' % attrs.as_html())


class Table(tables.Table):
    """Generic class with common properties for all tables."""
    ids = CustomCheckBoxColumn(accessor='pk',
                               orderable=False)

    class Meta:
        attrs = {"class": "paleblue"}
        sequence = ("ids", "...",)


class FilterSet(filters.FilterSet):
    """Generic class that allows filter for all the model fields."""
    class Meta:
        model = None
