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
    t = datetime.now()
    bundles = Bundle.objects.filter(table__day=t.weekday() + 1, table__start__lte=t, table__end__gte=t)
    if bundles.count() == 0:
        t = t + timedelta(minutes=20)
        bundles = Bundle.objects.filter(table__day=t.weekday() + 1, table__start__lte=t, table__end__gte=t)
    rooms = Room.objects.all()
    rooms = rooms.exclude(bundle__in=bundles)
    res = []
    for item in rooms:
        if len(item.number) == 3:
            res.append(item.number)
    res.sort()
    return res
