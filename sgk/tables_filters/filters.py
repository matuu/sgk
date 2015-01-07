#encoding=utf-8
from datetime import timedelta

from django import forms
from django.utils.safestring import mark_safe

from django_filters.filters import Filter, ChoiceFilter, ModelMultipleChoiceFilter
from cdc_utils.widgets import CustomModelSelectMultipleWidget


class DateCustomRangeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (forms.DateInput(attrs=attrs), forms.DateInput(attrs=attrs))
        super(DateCustomRangeWidget, self).__init__(widgets)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        inner = ' y '.join(rendered_widgets)
        return mark_safe('<div class="input-daterange">' + inner + '</div>')


class DateCustomRangeField(forms.MultiValueField):
    widget = DateCustomRangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.DateField(),
            forms.DateField(),
        )
        widget = DateCustomRangeWidget(attrs={
            'class': 'datepicker', 'placeholder': 'dd/mm/aaaa'})
        kwargs.update(widget=widget)
        super(DateCustomRangeField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return slice(*data_list)
        return None


class DateCustomRangeFilter(Filter):
    """
    Filter to select a start and end date
    """
    field_class = DateCustomRangeField

    def filter(self, qs, value):
        if value:
            if value.start and not value.stop:
                # only start
                lookup = '%s__gte' % self.name
                return qs.filter(**{lookup: value.start})
            elif value.stop and not value.start:
                # only stop
                lookup = '%s__lte' % self.name
                return qs.filter(**{lookup: value.stop + timedelta(days=1)})
            else:
                # both start and stop
                lookup = '%s__range' % self.name
                return qs.filter(**{lookup: (value.start, value.stop + timedelta(days=1))})

        return qs


class ChoiceWithEmptyFilter(ChoiceFilter):
    """
    Filter with any option (optional).
    """
    def __init__(self, choices, *args, **kwargs):
        CHOICES_FILTER = [('', '--------------'), ]
        CHOICES_FILTER.extend(list(choices))
        super(ChoiceWithEmptyFilter, self).__init__(choices=CHOICES_FILTER, *args, **kwargs)


class ModelSelectMultipleFilter(ModelMultipleChoiceFilter):

    def __init__(self, *args, **kwargs):
        super(ModelSelectMultipleFilter, self).__init__(*args, **kwargs)
        model = kwargs['queryset'].model
        self.widget = CustomModelSelectMultipleWidget(model, self.label, is_stacked=False)
