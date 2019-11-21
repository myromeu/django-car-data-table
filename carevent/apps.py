import os
import sys
from django.apps import AppConfig


class CareventConfig(AppConfig):
    name = 'carevent'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        from .models import CarEvent
        from django.conf import settings
        import json

        with open(os.path.join(settings.BASE_DIR, 'table-data.json'), encoding='utf-8') as table_data:
            json_data = json.loads(table_data.read())

            for car in json_data:
                if not CarEvent.objects.filter(ordNumber=car['ordNumber']).exists():
                    CarEvent.create(**car)
