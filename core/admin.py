from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Table)
admin.site.register(Subject)
admin.site.register(Tutor)
admin.site.register(Room)
admin.site.register(Group)