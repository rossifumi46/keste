from django.db import models
from django.utils import timezone

from time import strftime

# Create your models here.

DAY_CHOICES = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
)


class Table(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAY_CHOICES)
    bundle = models.ForeignKey('Bundle', on_delete=models.CASCADE)
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    block = models.ForeignKey('Block', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.subject.name + ' | ' + self.tutor.name + ' | ' + self.start.strftime("%H:%M")


class Group(models.Model):
    group = models.CharField(max_length=10)
    year = models.IntegerField()
    lang = models.CharField(max_length=2)
    number = models.IntegerField()

    def course(self):
        return timezone.now().year - self.year

    def __str__(self):
        return self.group


class Tutor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=30, default="0")

    def __str__(self):
        return self.number


class Bundle(models.Model):
    room = models.ManyToManyField(Room)
    ID = models.IntegerField()

    def __str__(self):
        return str(self.ID)

class Block(models.Model):
    name = models.CharField(max_length=150)
