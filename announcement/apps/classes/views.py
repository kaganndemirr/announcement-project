from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings
from django.utils.timezone import localtime

from datetime import date, datetime
from .models import Lecture, Exam, LectureSession

class AjaxLectures(View):
    def get(self, request):
        weekday = date.today().weekday()
        data = [
            {
                'code': lec.l_code,
                'name': lec.title,
                'lecturer': lec.lecturer,
                'time': localtime(ses.s_date).strftime('%H:%M'),
                'duration': ses.duration,
                'location': ses.location,
            }

            for lec in Lecture
                    .objects
                    .filter(department=request.user.department)
            for ses in LectureSession
                    .objects
                    .filter(lecture=lec)
                    .order_by('s_date')
            if localtime(ses.s_date).weekday() == weekday
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
                        e_date__date__gte=datetime.utcnow().date())
                    .order_by('e_date')
        ]
        return JsonResponse({"exams": list(data)})
