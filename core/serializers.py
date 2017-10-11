from rest_framework import serializers
from core.models import *


class SubjectGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TutorGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class RoomGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BlockGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    tutor = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = '__all__'

    def get_subject(self, model):
        return SubjectGetSerializer(model.subject).data

    def get_tutor(self, model):
        return TutorGetSerializer(model.tutor).data

    def get_room(self, model):
        return RoomGetSerializer(model.room).data
