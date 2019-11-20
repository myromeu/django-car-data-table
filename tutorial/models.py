from django.db import models
from collections import OrderedDict


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")


class CarEvent(models.Model):
    ordNumber = models.IntegerField(primary_key=True)  # 1,
    carNumber = models.CharField(max_length=16)  # "94003894",
    trainIndex = models.CharField(max_length=16, null=True, blank=True)  # "035004766035601",
    trainNumber = models.CharField(max_length=16, null=True, blank=True)  # "9999",
    carStatus = models.CharField(max_length=64, blank=True)  # "составлен в поезд",
    invoiceId = models.CharField(max_length=16)  # "923210370",
    invoiceNumber = models.CharField(max_length=16)  # "ЭО560089",
    stateId = models.IntegerField()  # 34,
    lastOperDt = models.DateTimeField(null=True, blank=True)  # "2019-08-11T20:51:00.000Z"

    labels = OrderedDict([("ordNumber", '№ п/п'),
                          ("carNumber", 'Номер вагона'),
                          ("trainIndex", 'Индекс поезда'),
                          ("trainNumber", 'Номер поезда'),
                          ("carStatus", 'Статус'),
                          ("invoiceId", 'ИД накладной'),
                          ("invoiceNumber", '№ накладной'),
                          ("stateId", 'stateId'),
                          ("lastOperDt", 'Дата-время операции')])

    @classmethod
    def create(cls, **kwargs):
        carevent, _ = cls.objects.get_or_create(
            ordNumber=kwargs["ordNumber"],
            carNumber=kwargs["carNumber"],
            trainIndex=kwargs["trainIndex"],
            trainNumber=kwargs["trainNumber"],
            carStatus=kwargs["carStatus"],
            invoiceId=kwargs["invoiceId"],
            invoiceNumber=kwargs["invoiceNumber"],
            stateId=kwargs["stateId"],
            lastOperDt=kwargs["lastOperDt"],
        )
        return carevent
