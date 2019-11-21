from django import forms

from .models import CarEvent


class CarEventForm(forms.ModelForm):
    class Meta:
        model = CarEvent
        fields = tuple(CarEvent.labels.keys())
        labels = CarEvent.labels

    def __init__(self, *args, **kwargs):
        super(CarEventForm, self).__init__(*args, **kwargs)
        readonlyfields = dict([("ordNumber", '№ п/п'),
                               ("carNumber", 'Номер вагона'),
                               ("trainIndex", 'Индекс поезда'),
                               ("carStatus", 'Статус'),
                               ("stateId", 'stateId')])
        for key in readonlyfields.keys():
            self.fields[key].widget.attrs['readonly'] = True
