from .models import *

from datetime import time

from django.db.models import Q
from datetime import datetime, timedelta
import pprint

def check_demand(rooms, start, end):
    """
    Search rooms which are free between start and end.
    """
    result = []
    if rooms is None:
        return result

    end = time(end.hour, end.minute - 1)

    schedules = Table.objects.filter(Q(start__gte=start, start__lt=end) |
                                        Q(end__gt=start, end__lte=end))
    print(schedules)
    rooms = rooms.exclude(schedule__in=schedules)
    for room in rooms:
        temp = {
            'room': room.number
        }
        result.append(temp)
    return schedules


def free():
    time = datetime.now()
    bundles = Bundle.objects.filter(table__day=time.weekday() + 1, table__start__lte=time, table__end__gte=time)
    if bundles.count() == Bundle.objects.all().count():
        time = time + timedelta(minutes=10)
    bundles = Bundle.objects.filter(table__day=time.weekday() + 1, table__start__lte=time.time(), table__end__gte=time.time())
    rooms = Room.objects.all()
    rooms = rooms.exclude(bundle__in=bundles)
    return rooms
