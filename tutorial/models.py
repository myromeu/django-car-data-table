from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")


class CarEvent(models.Model):
    ordNumber = models.IntegerField(primary_key=True)  # 1,
    carNumber = models.CharField(max_length=16)  # "94003894",
    trainIndex = models.CharField(max_length=16, null=True, blank=True) # "035004766035601",
    trainNumber = models.CharField(max_length=16, null=True, blank=True)    # "9999",
    carStatus = models.CharField(max_length=64, blank=True)  # "составлен в поезд",
    invoiceId = models.CharField(max_length=16)  # "923210370",
    invoiceNumber = models.CharField(max_length=16)  # "ЭО560089",
    stateId = models.IntegerField()    # 34,
    lastOperDt = models.DateTimeField(null=True, blank=True) # "2019-08-11T20:51:00.000Z"

    @staticmethod
    def create(**kwargs):
        movie = .objects.create(
            popularity=kwargs['99popularity'],
            director=kwargs['director'],
            imdb_score=kwargs['imdb_score'],
            name=kwargs['name']
        )
        for genre_name in kwargs['genre']:
            genre, created = Genre.objects.get_or_create(name=genre_name)
            movie.genre.add(genre)
        return movie