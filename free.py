import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'schedule.settings')
import django

django.setup()

import requests
import json
import pprint
from core.models import *
import datetime
from core import utils

if __name__ == "__main__":
    time = datetime.datetime.now()
    bundles = Bundle.objects.filter(table__day=time.weekday()+1, table__start__lte=time, table__end__gte=time)
    # tables = Table.objects.filter(start__lte=time.time(), end__gte=time.time(), day=time.weekday() + 1)
    # for table in tables:
    #     print(table)
    rooms = Room.objects.all()
    rooms = rooms.exclude(bundle__in=bundles)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(res)
    for item in rooms:
        print(item)