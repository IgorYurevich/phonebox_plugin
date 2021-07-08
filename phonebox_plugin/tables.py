import django_tables2 as tables
from .models import Number, NumbersRange
from utilities.tables import BaseTable, ToggleColumn


class NumberTable(BaseTable):

    pk = ToggleColumn()
    number = tables.LinkColumn()
    tenant = tables.LinkColumn()
    region = tables.LinkColumn()
    provider = tables.LinkColumn()
    forward_to = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Number
        fields = ('pk', 'number', 'tenant', 'region', 'description', 'provider', 'forward_to')

class NumbersRangeTable(BaseTable):

    pk = ToggleColumn()
    start = tables.LinkColumn()
    end = tables.LinkColumn()
    tenant = tables.LinkColumn()
    region = tables.LinkColumn()
    provider = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = NumbersRange
        fields = ('pk', 'start', 'end', 'tenant', 'region', 'description', 'provider')
