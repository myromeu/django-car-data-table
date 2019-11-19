import sys
import os
from django.apps import AppConfig


class TutorialConfig(AppConfig):
    name = 'tutorial'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        from .models import CarEvent
        from django.conf import settings
        import json

        with open(os.path.join(settings.BASE_DIR, 'table-data.json')) as table_data:
            json_data = json.loads(table_data.read())

            for car in json_data:
                # make CarEvent objects
                # on stop server truncate the objects mb not
                car_event = CarEvent.create(**car)