import django_tables2 as tables
from .models import Person, CarEvent
import django_filters


class CarEventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = CarEvent
        fields = tuple(CarEvent.labels.keys())


class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name",)


class CarEventTable(tables.Table):
    class Meta:
        model = CarEvent
        template_name = "django_tables2/cartable.html"
        fields = tuple(CarEvent.labels.keys())

    def change_header(self, col_names={}):
        for key, value in col_names.items():
            self.base_columns[key].verbose_name = value

    def render_lastOperDt(self, value):
        import datetime
        if value:
            return value.strftime('%d.%m.%Y %H:%M')
        else:
            return '–'
