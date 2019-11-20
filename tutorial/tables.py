import django_tables2 as tables
from .models import Person, CarEvent


class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name",)


class CarEventTable(tables.Table):
    class Meta:
        model = CarEvent
        template_name = "django_tables2/bootstrap4.html"
        fields = ("ordNumber",
                  "carNumber",
                  "trainIndex",
                  "trainNumber",
                  "carStatus",
                  "invoiceId",
                  "invoiceNumber",
                  "stateId",
                  "lastOperDt",)
