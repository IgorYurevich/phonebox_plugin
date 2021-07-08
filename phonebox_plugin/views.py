#!./venv/bin/python

from netbox.views import generic
from .models import Number, NumbersRange
from . import filters
from . import forms
from . import tables


class NumberListView(generic.ObjectListView):
    queryset = Number.objects.all()
    filterset = filters.NumberFilterSet
    filterset_form = forms.NumberFilterForm
    table = tables.NumberTable
    template_name = "phonebox_plugin/list_view.html"


class NumberView(generic.ObjectView):
    queryset = Number.objects.prefetch_related('tenant')


class NumberEditView(generic.ObjectEditView):
    queryset = Number.objects.all()
    model_form = forms.NumberEditForm
    template_name = "phonebox_plugin/add_number.html"


class NumberBulkEditView(generic.BulkEditView):
    queryset = Number.objects.prefetch_related('tenant')
    filterset = filters.NumberFilterSet
    table = tables.NumberTable
    form = forms.NumberBulkEditForm


class NumberDeleteView(generic.ObjectDeleteView):
    queryset = Number.objects.all()
    default_return_url = "plugins:phonebox_plugin:list_view"


class NumberBulkDeleteView(generic.BulkDeleteView):
    queryset = Number.objects.filter()
    filterset = filters.NumberFilterSet
    table = tables.NumberTable
    default_return_url = "plugins:phonebox_plugin:list_view"


# NumbersRange

class NumbersRangeListView(generic.ObjectListView):
    queryset = NumbersRange.objects.all()
    filterset = filters.NumbersRangeFilterSet
    filterset_form = forms.NumbersRangeFilterForm
    table = tables.NumbersRangeTable
    template_name = "phonebox_plugin/range_list_view.html"


class NumbersRangeView(generic.ObjectView):
    queryset = NumbersRange.objects.prefetch_related('tenant')


class NumbersRangeEditView(generic.ObjectEditView):
    queryset = NumbersRange.objects.all()
    model_form = forms.NumbersRangeEditForm
    template_name = "phonebox_plugin/add_range.html"


class NumbersRangeBulkEditView(generic.BulkEditView):
    queryset = NumbersRange.objects.prefetch_related('tenant')
    filterset = filters.NumbersRangeFilterSet
    table = tables.NumbersRangeTable
    form = forms.NumbersRangeBulkEditForm


class NumbersRangeDeleteView(generic.ObjectDeleteView):
    queryset = NumbersRange.objects.all()
    default_return_url = "plugins:phonebox_plugin:range_list_view"


class NumbersRangeBulkDeleteView(generic.BulkDeleteView):
    queryset = NumbersRange.objects.filter()
    filterset = filters.NumbersRangeFilterSet
    table = tables.NumbersRangeTable
    default_return_url = "plugins:phonebox_plugin:range_list_view"
