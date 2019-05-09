from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.timezone import localtime

from datetime import date
from .models import Slide, Announcement, Event
from .variables import ACTIVE

class AjaxAnnouncement(View):
    def get(self, request):
        data = [
            i['title']
            for i in Announcement
                    .objects
                    .filter(department=request.user.department)
                    .order_by('creation_date').values()
        ]
        return JsonResponse({"announcements": list(data)})

class AjaxSlides(View):
    def get(self, request):
        data = [
            {
                'title': i['title'],
                'content': i['data'],
                'type': i['type']
            }

            for i in Slide
                    .objects
                    .filter(department=request.user.department, status=ACTIVE)
                    .order_by('-creation_time').values()
        ]
        return JsonResponse({"slides": list(data)})

class AjaxEvents(View):
    def get(self, request):
        data = [
            {
                'datetime': localtime(i['date']).strftime('%d/%m/%Y %H:%M'),
                'title': i['name'],
                'location': i['location'],
            }

            for i in Event
                    .objects
                    .filter(department=request.user.department,
                        date__date__gte=date.today())
                    .order_by('date').values()
        ]
        return JsonResponse({"events": list(data)})
