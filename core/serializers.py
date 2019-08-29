from rest_framework import serializers
from core.models import *


class SubjectGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        # fields = '__all__'
        exclude = ('id',)


class TutorGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        # fields = '__all__'
        exclude = ('id',)


class RoomGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # fields = '__all__'
        exclude = ('id',)


class BlockGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = ('name',)

class TableSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    tutor = serializers.SerializerMethodField()
    block = serializers.SerializerMethodField()
    bundle = serializers.SerializerMethodField()

    class Meta:
        model = Table
        exclude = ('bundle', 'created', 'id', 'day', 'start', 'end')

    def get_subject(self, model):
        # print(SubjectGetSerializer(model.subject).data)
        return SubjectGetSerializer(model.subject).data['name']

    def get_tutor(self, model):
        return TutorGetSerializer(model.tutor).data['name']

    def get_block(self, model):
        return BlockGetSerializer(model.block).data['name']

    def get_bundle(self, model):
        rooms=Room.objects.filter(bundle=model.bundle)
        return RoomGetSerializer(rooms, many=True).data


# class ScheduleSerializer(serializers.Serializer):
#     def create(self, validated_data):
