from django.contrib import admin

from .models import *
# Register your models here.

# class BlockAdmin(admin.ModelAdmin):
#     model = Block
#     list_display = ('name', 'description',)

admin.site.register(Table)
admin.site.register(Subject)
admin.site.register(Tutor)
admin.site.register(Room)
admin.site.register(Group)
admin.site.register(Bundle)
admin.site.register(Block)
