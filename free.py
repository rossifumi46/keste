import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'schedule.settings')
import django

django.setup()

import requests
import json
import pprint
from core.models import *
from datetime import datetime, time
from core import utils

if __name__ == "__main__":
    rooms  = utils.check(1, time(9), time(9, 50))
    for room in rooms:
        print(room)