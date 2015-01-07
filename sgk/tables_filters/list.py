from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django import forms
from django_tables2 import SingleTableMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from cdc_utils import export


class ListFilteredMixin(object):
    """
    Mixin that adds support for django-filter
    """

    filter_set = None

    def get_filter_set(self):
        if self.filter_set:
            return self.filter_set
        else:
            raise ImproperlyConfigured(
                "ListFilterMixin requires either a definition of "
                "'filter_set' or an implementation of 'get_filter()'")

    def get_filter_set_kwargs(self):
        """
        Returns the keyword arguments for instanciating the filterset.
        """
        return {
            'data': self.request.GET,
            'queryset': self.get_base_queryset(),
        }

    def get_base_queryset(self):
        """
        We can decided to either alter the queryset before or after
        applying the FilterSet
        """
        return super(ListFilteredMixin, self).get_queryset()

    def get_constructed_filter(self):
        # We need to store the instantiated FilterSet cause we use it in
        # get_queryset and in get_context_data
        if hasattr(self, 'constructed_filter'):
            return self.constructed_filter
        else:
            f = self.get_filter_set()(**self.get_filter_set_kwargs())
            self.constructed_filter = f
            return f

    def get_queryset(self):
        return self.get_constructed_filter().qs

    def get_context_data(self, **kwargs):
        kwargs.update({'filter': self.get_constructed_filter()})
        return super(ListFilteredMixin, self).get_context_data(**kwargs)


class ListFilteredView(ListFilteredMixin, ListView):
    """
    A list view that can be filtered by django-filter
    """


class Tables2Mixin(SingleTableMixin):
    """
    Mixin that adds support for django-tables2
    """
    queryset = "non_assign"
    table_class = None
    # If None, context_table_name = 'table'
    context_table_name = 'filter_qs'
    # If None, pagination default is enabled
    table_pagination = None
    # Add extra field when export
    extra_fields_to_export = None
    # if display constant or descriptions
    display_description = False
    # Ignore field when export list
    fields_ignore_to_export = []

    def get_queryset(self):
        if self.queryset != 'non_assign':
            return self.queryset
        else:
            raise ImproperlyConfigured(
                "Tables2Mixin requires either a definition of 'queryset' "
                "or 'model', or an implementation of 'get_queryset()'")


class Tables2View(Tables2Mixin, ListView):
    """
    A list view rendering by django-tables2.
    """
    # Default Template Name
    # template_name = "[model_template_dir]/[model_name]_list.html"


class ActionsForm(forms.Form):
    action = forms.IntegerField()


class SelectionForm(forms.Form):
    #ids = forms.TypedMultipleChoiceField(coerce=int)
    all = forms.BooleanField(initial=False, required=False)


class TablesFilteredView(ListFilteredMixin, Tables2Mixin, ListView):
    """
    A list view that can be filtered by django-filter
    and render table by django-tables2.
    """

    actions = [export.export_csv, ]

    def get_table_data(self):
        if hasattr(self, "get_constructed_filter"):
            return self.get_constructed_filter().qs
        else:
            return super(Tables2Mixin, self).get_table_data()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """
        Only authenticated users view the list of objects.
        """
        return super(ListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(TablesFilteredView, self).get_context_data(*args, **kwargs)
        descriptions = []
        for action in self.actions:
            action_description = getattr(action, 'short_description', action.__name__)
            attrs = getattr(action, 'attrs', {})
            descriptions.append((action_description, attrs))
        context['actions'] = descriptions
        return context

    def post(self, request, *args, **kwargs):
        isOk = True
        actions_form = ActionsForm(self.request.POST)
        if actions_form.is_valid():
            if actions_form.cleaned_data['action'] != -1:
                try:
                    action = self.actions[actions_form.cleaned_data['action'] - 1]
                except IndexError:
                    isOk = False
                selection_form = SelectionForm(self.request.POST)
                if not selection_form.is_valid():
                    isOk = False
                queryset = self.get_queryset()
                if not queryset:
                    messages.add_message(request, messages.ERROR,
                                         u"Debe seleccionar al menos un registro.")
                    isOk = False
                if not selection_form.cleaned_data['all'] and isOk:
                    if not len(self.request.POST.getlist("ids")):
                        messages.add_message(request, messages.ERROR,
                                             u'Debe seleccionar al menos un registro')
                        isOk = False
                    queryset = queryset.filter(pk__in=self.request.POST.getlist('ids'))
                if isOk:
                    if isinstance(action, basestring):
                        return getattr(self, action)(self, queryset)
                    else:
                        return action(self, queryset)
        return super(TablesFilteredView, self).get(request, *args, **kwargs)
