from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings
from django.utils.timezone import localtime

from datetime import date
from .models import Lecture, Exam

class AjaxLectures(View):
    def get(self, request):
        weekday = date.today().weekday()
        data = [
            {
                'code': i.l_code,
                'name': i.title,
                'lecturer': i.lecturer,
                'time': localtime(i.l_date).strftime('%H:%M'),
            }

            for i in Lecture
                    .objects
                    .filter(department=request.user.department)
                    .order_by('l_date')
            if i.l_date.weekday() == weekday
        ]
        return JsonResponse({"lectures": list(data)})

class AjaxExams(View):
    def get(self, request):
        data = [
            {
                'code': i.lecture.l_code,
                'name': i.lecture.title,
                'lecturer': i.lecture.lecturer,
                'datetime': localtime(i.e_date).strftime('%d/%m/%Y %H:%M'),
                'location': i.location,
                'duration': i.duration,
            }

            for i in Exam
                    .objects
                    .filter(lecture__department=request.user.department,
                        e_date__date__gte=date.today())
                    .order_by('e_date')
        ]
        return JsonResponse({"exams": list(data)})
