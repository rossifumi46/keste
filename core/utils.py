from .models import *

from datetime import time

from django.db.models import Q
from datetime import datetime, timedelta


def check(day, start, end):
    """
    Search rooms which are free between start and end.
    """
    result = []

    rooms = Room.objects.all()

    bundles = Bundle.objects.filter(Q(table__start__gte=start, table__start__lt=end) |
                                    Q(table__end__gt=start, table__end__lte=end) |
                                    Q(table__start__lt=start, table__end__gt=end),
                                    Q(table__day=day))
    rooms = rooms.exclude(bundle__in=bundles)
    for item in rooms:
        if len(item.number) == 3:
            result.append(item.number)
    result.sort()
    return result


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
