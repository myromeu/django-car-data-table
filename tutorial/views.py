from django.shortcuts import render

from django.views.generic import ListView
from django_tables2 import SingleTableView

from .models import Person
from .tables import PersonTable


# class PersonListView(ListView):
#     model = Person
#     template_name = 'tutorial/people.html'


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'tutorial/people2.html'
