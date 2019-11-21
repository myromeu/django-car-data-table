from django.shortcuts import render, redirect

from django.views.generic import ListView
from django_tables2 import SingleTableView

from tutorial.forms import CarEventForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'].change_header(CarEvent.labels)
        context['table'].default = ''
        context['table'].paginate(page=self.request.GET.get("page", 1), per_page=10)

        if 'edit' in self.request.GET:
            form = CarEventForm(instance=CarEvent.objects.get(ordNumber=self.request.GET['edit']))
            context['careventform'] = form
        return context

    def post(self, *args, **kwargs):
        carevent = CarEvent.objects.get(ordNumber=self.request.POST['ordNumber'])
        form = CarEventForm(self.request.POST, instance=carevent)
        if form.is_valid():
            form.save()

        return redirect('car_events')


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'tutorial/people2.html'
