from datetime import datetime, timedelta

from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
from django.http import Http404
from django.shortcuts import render
from django.db.models import Max, Min
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from core.serializers import *
from core.models import *
from core import utils
from core.forms import FindForm


class BlockView(APIView):
    def get_table(self, pk):
        try:
            block = Block.objects.get(pk=pk)
            my = block.my.all()
            min = Table.objects.filter(block__in=my).aggregate(Min('time'))['time__min']
            max = Table.objects.filter(block__in=my).aggregate(Max('time'))['time__max']
            table = {}
            t = datetime.now()
            d = t.weekday() + 1
            # if d > 5:
            #     d = 1
            #     first = True
            # table[str(1)][str(item['time'])]["next"] = True
            next = False
            before = False
            after = False
            for i in range(1, 6):
                tables = Table.objects.filter(day=i, block__in=my).order_by('start')
                if d == i:
                    s = tables.aggregate(Min('start'))['start__min']
                    e = tables.aggregate(Max('end'))['end__max']
                    if t.time() < s:
                        before = True
                    if t.time() > e:
                        after = True

                serializer = TableSerializer(tables, many=True)
                table[str(i)] = {}
                for j in range(min, max + 1):
                    table[str(i)][str(j)] = None
                e = Time.objects.get(pk=1).start
                for item in serializer.data:

                    table[str(i)][str(item['time'])] = item

                    time = Time.objects.get(pk=int(item['time']))
                    s = time.start

                    if d == i and before and item['time'] == time.pk:
                        table[str(i)][str(item['time'])]["pre"] = True
                        before = False
                    else:
                        table[str(i)][str(item['time'])]["pre"] = False
                    if d == i and e < t.time() < s:
                        table[str(i)][str(item['time'])]["pre"] = True
                    e = time.end
                    if next:
                        table[str(i)][str(item['time'])]["pre"] = True
                        next = False
                    if s < t.time() < e and d == i:
                        table[str(i)][str(item['time'])]["now"] = True
                        next = True
                    else:
                        table[str(i)][str(item['time'])]["now"] = False
                    if d + 1 == i and after:
                        table[str(i)][str(item['time'])]["pre"] = True
                        after = False

            return table
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        table = self.get_table(pk=pk)
        return Response(table, status=status.HTTP_200_OK)


class TutorView(APIView):
    def get_table(self, pk):
        try:
            tutor = Tutor.objects.get(pk=pk)
            table = {}
            t = datetime.now()
            d = t.weekday() + 1
            # if d > 5:
            #     d = 1
            #     first = True
            # table[str(1)][str(item['time'])]["next"] = True
            next = False
            before = False
            after =False
            min = Table.objects.filter(tutor=tutor).aggregate(Min('time'))['time__min']
            max = Table.objects.filter(tutor=tutor).aggregate(Max('time'))['time__max']
            for i in range(1, 6):
                tables = Table.objects.filter(day=i, tutor=tutor).order_by('start')
                if d == i:
                    s = tables.aggregate(Min('start'))['start__min']
                    e = tables.aggregate(Max('end'))['end__max']
                    if t.time() < s:
                        before = True
                    if t.time() > e:
                        after = True
                serializer = TableSerializer(tables, many=True)
                table[str(i)] = {}
                for j in range(min, max+1):
                    table[str(i)][str(j)] = None
                for item in serializer.data:
                    if next:
                        table[str(i)][str(item['time'])]["pre"] = True
                        next = False
                    table[str(i)][str(item['time'])] = item
                    time = Time.objects.get(pk=int(item['time']))
                    sl = time.start
                    el = time.end
                    if sl < t.time() < el and d == i:
                        table[str(i)][str(item['time'])]["now"] = True
                        next = True
                    else:
                        table[str(i)][str(item['time'])]["now"] = Fals
                    if d == i and before and item['time'] == s:
                        table[str(i)][str(item['time'])]["pre"] = True
                        before = False
                    else:
                        table[str(i)][str(item['time'])]["pre"] = False
                    if d+1 == i and after:
                        table[str(i+1)][str(item['time'])]["pre"] = True
                        after = False
                    else:
                        table[str(i)][str(item['time'])]["pre"] = False
                next = False

            return table
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        table = self.get_table(pk=pk)
        return Response(table, status=status.HTTP_200_OK)


class RoomView(APIView):
    def get_table(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            table = {}
            d = datetime.now().weekday() + 1
            first = False
            if d > 5:
                d = 1
                first = True
            # table[str(1)][str(item['time'])]["next"] = True
            next = False
            after = False
            min = Table.objects.filter(bundle__room=room).aggregate(Min('time'))['time__min']
            max = Table.objects.filter(bundle__room=room).aggregate(Max('time'))['time__max']
            for i in range(1, 6):
                tables = Table.objects.filter(day=i, bundle__room=room).order_by('start')
                l = 0
                if d == i:
                    s = tables.aggregate(Min('time'))['time__min']
                    if not first:
                        e = tables.aggregate(Max('time'))['time__max']
                        sh = Time.objects.get(pk=s)
                        eh = Time.objects.get(pk=e)
                        l = 0
                        if next:
                            l = s
                        else:
                            if datetime.now().time() < sh.start:
                                l = s
                            else:
                                if datetime.now().time() > eh.start:
                                    d = d + 1
                                    next = True
                                else:
                                    after = True

                serializer = TableSerializer(tables, many=True)
                # table[str(i)] = serializer.data
                table[str(i)] = {};
                for j in range(min, max+1):
                    table[str(i)][str(j)] = None
                af = False
                for item in serializer.data:
                    table[str(i)][str(item['time'])] = item
                    t = False
                    t1 = False
                    if d == i and l == item['time']:
                        t1 = True
                    if first:
                        t1 = True
                        first = False
                    table[str(i)][str(item['time'])]["pre"] = t1
                    time = Time.objects.get(pk=int(item['time']))
                    s = time.start
                    e = time.end
                    if af and table[str(i)][str(item['time'])] != None:
                        table[str(i)][str(item['time'])]["pre"] = True
                        af = False
                    if s < datetime.now().time() < e and i == datetime.now().weekday() + 1 and not next:
                        t =True
                        if after:
                            af = True
                            after = False
                    table[str(i)][str(item['time'])]["now"] = t


            return table
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        table = self.get_table(pk=pk)
        return Response(table, status=status.HTTP_200_OK)


@api_view(['GET'])
def search(request):
    query = request.GET.get('query', None)

    block = Block.objects.annotate(distance=TrigramDistance('name', query), sim=TrigramSimilarity('name', query))\
                         .filter(distance__lt=0.9, sim__gt=0.2)\
                         .order_by('distance')[:5]

    tutor = Tutor.objects.annotate(sim=TrigramSimilarity('name', query)) \
                .filter(sim__gt=0.1) \
                .order_by('-sim')[:5]
    room = Room.objects.annotate(distance=TrigramDistance('number', query), sim=TrigramSimilarity('number', query)) \
                .filter(distance__lt=0.7, sim__gt=0.1) \
                .order_by('distance')[:5]

    data = []
    t = datetime.now()
    for item in block:
        b = Block.objects.filter(block=item)
        bundle = Bundle.objects.filter(table__block__in=b, table__day=t.weekday()+1, table__start__lt=t.time(), table__end__gt=t.time())
        t1 = t + timedelta(hours=1, minutes=20)
        if bundle.exists():
            now = False
        else:
            now = True
        bundles = Bundle.objects.filter(table__block__in=b,
                                       table__day=t.weekday() + 1,
                                       table__end__lt=t1.time(),
                                       table__start__gt=t.time())

        if now:
            bundle = bundle.union(bundles)
        rooms = []
        if bundle.exists():
            room = Room.objects.filter(bundle=bundle[0])

            for value in room:
                    rooms.append(value.number)
        data.append(
            {
                "name": item.name,
                "id": item.id,
                "info": rooms,
                "type": 'block',
                "now": now
            }
        )

        # if bundles.exists():
        #     room = Room.objects.filter(bundle=bundles[0])
        #     for value in room:
        #             rooms.append(value.number)
        # data.append(
        #     {
        #         "name": item.name,
        #         "id": item.id,
        #         "info": rooms,
        #         "type": 'block'
        #     }
        # )

    for item in tutor:
        try:
            table = Table.objects.get(tutor=item, day=t.weekday()+1, start__lt=t.time(), end__gt=t.time())
            data.append(
                {
                    "name": item.name,
                    "id": item.id,
                    "info": {table.bundle.room.all()[0].number, table.block.name, table.subject.name},
                    "type": 'tutor'
                }
            )
        except:
            data.append(
                {
                    "name": item.name,
                    "id": item.id,
                    "type": 'tutor'
                }
            )

    for item in room:
        data.append(
            {
                "name": item.number,
                "id": item.id,
                # "room": rooms,
                "type": 'room'
            }
        )

    return Response(data)


def free(request):
    rooms = utils.free()
    return render(request, 'free.html',  {'rooms': rooms})

def index(request):
    return render(request, 'index.html')

def find(request):
    if request.method == 'GET':
        form = FindForm()
        rooms = None
        return render(request, 'find.html', {'form': form, 'rooms': rooms})
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            day = form.cleaned_data['day']
            rooms = utils.check(day, start, end)
            form = FindForm(request.POST)
            return render(request, 'find.html', {'form': form, 'rooms': rooms})
