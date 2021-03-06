# Django
from django.contrib import admin

# Local

from .models import *


@admin.register(Department)
class DeparmentAdmin(admin.ModelAdmin):
    fields = ('d_code', 'name')

    list_display = ('d_code', 'name')

    def get_queryset(self, request):
        qs = super(DeparmentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(d_code=request.user.department)


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    fields = ('creation_time', 'title', 'data', 'type', 'status')

    list_display = ('creation_time', 'department', 'title', 'data', 'type', 'status')

    def get_queryset(self, request):
        qs = super(SlideAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(department=request.user.department)

    def save_model(self, request, obj, form, change):
        obj.department = request.user.department
        super().save_model(request, obj, form, change)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('date', 'name', 'location')

    list_display = ('date', 'department', 'name', 'location')

    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(department=request.user.department)

    def save_model(self, request, obj, form, change):
        obj.department = request.user.department
        super().save_model(request, obj, form, change)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    fields = ('creation_date', 'title')

    list_display = ('creation_date', 'department', 'title')

    def get_queryset(self, request):
        qs = super(AnnouncementAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(department=request.user.department)

    def save_model(self, request, obj, form, change):
        obj.department = request.user.department
        super().save_model(request, obj, form, change)
