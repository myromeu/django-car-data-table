from django.shortcuts import redirect

from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .forms import CarEventForm
from .models import CarEvent
from .tables import CarEventTable, CarEventFilter


def remove_table_data(request):
    for ce in CarEvent.objects.all():
        print(f'deleting {ce.ordNumber}')
        ce.delete()
    return redirect('car_events')


class CarEventListView(SingleTableMixin, FilterView):
    model = CarEvent
    table_class = CarEventTable
    filterset_class = CarEventFilter
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
