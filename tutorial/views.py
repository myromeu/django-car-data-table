from django.shortcuts import render, redirect

from django.views.generic import ListView
from django_tables2 import SingleTableView

from .models import Person, CarEvent
from .tables import PersonTable, CarEventTable


# class PersonListView(ListView):
#     model = Person
#     template_name = 'tutorial/people.html'

def remove_table_data(request):
    for ce in CarEvent.objects.all():
        print(f'deleting {ce.ordNumber}')
        ce.delete()
    return redirect('car_events')


class CarEventListView(SingleTableView):
    model = CarEvent
    table_class = CarEventTable
    template_name = 'tutorial/carevents.html'


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'tutorial/people2.html'
