from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from datetime import date
from .models import Lecture, Exam

class AjaxLectures(View):
    def get(self, request):
        data = [
            {
                'code': i.l_code,
                'name': i.title,
                'lecturer': i.lecturer,
                'time': i.l_date.time(),
            }

            for i in Lecture
                    .objects
                    .filter(department=request.user.department,
                        l_date__date__gte=date.today())
                    .order_by('l_date')
        ]
        return JsonResponse({"lectures": list(data)})

class AjaxExams(View):
    def get(self, request):
        data = [
            {
                'code': i.lecture.l_code,
                'name': i.lecture.title,
                'lecturer': i.lecture.lecturer,
                'datetime': i.e_date,
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
