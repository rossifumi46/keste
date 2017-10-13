from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework import status
from rest_framework.decorators import api_view

from core.serializers import *
from core.models import *
from core import utils
from core.forms import FindForm

class Block(APIView):
    def get_table(self, pk):
        try:
            block = Block.objects.get(pk=pk)
            table = {}
            for i in range(1, 6):
                tables = Table.objects.filter(day=i, block=block)
                serializer = TableSerializer(tables, many=True)
                table[str(i)] = serializer.data
            return table
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        table = self.get_table(pk=pk)
        return Response(table, status=status.HTTP_200_OK)


class Tutor(APIView):
    def get_table(self, pk):
        try:
            tutor = Tutor.objects.get(pk=pk)
            table = {}
            for i in range(1, 6):
                tables = Table.objects.filter(day=i, tutor=tutor)
                serializer = TableSerializer(tables, many=True)
                table[str(i)] = serializer.data
            return table
        except Group.DoesNotExist:
            raise Http404

    def get(self, pk):
        table = self.get_table(pk=pk)
        return Response(table, status=status.HTTP_200_OK)


class Room(APIView):
    def get_table(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            table = {}
            for i in range(1, 6):
                tables = Table.objects.filter(day=i, room=room)
                serializer = TableSerializer(tables, many=True)
                table[str(i)] = serializer.data
            return table
        except Group.DoesNotExist:
            raise Http404

    def get(self, pk):
        table = self.get_table(pk=pk)
        return Response(table, status=status.HTTP_200_OK)


@api_view(['GET'])
def search(request):
    query = request.GET.get('query', None)

    room = Room.objects.filter(number__icontains=query)

    room = RoomGetSerializer(room, many=True)

    tutor = Tutor.objects.filter(name__icontains=query)

    tutor = TutorGetSerializer(tutor, many=True)

    block = Block.objects.filter(name__icontains=query)

    block = BlockGetSerializer(block, many=True)

    data = {
        'room': room.data,
        'block': block.data,
        'tutor': tutor.data
    }
    return Response(data)


def free(request):
    rooms = utils.free()
    return render(request, 'free.html',  {'rooms': rooms})


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