from django.contrib import admin

from rooms.models import RoomType


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity',)


