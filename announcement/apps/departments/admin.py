# Django
from django.contrib import admin

# Local

from .models import *


@admin.register(Department)
class DeparmentAdmin(admin.ModelAdmin):
    fields = ('d_code', 'name')

    list_display = ('d_code', 'name')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    fields = ('creation_time', 'department', 'title', 'data', 'type', 'status')

    list_display = ('creation_time', 'department', 'title', 'data', 'type', 'status')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('date', 'department', 'name', 'location')

    list_display = ('date', 'department', 'name', 'location')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    fields = ('creation_date', 'department', 'title')

    list_display = ('creation_date', 'department', 'title')