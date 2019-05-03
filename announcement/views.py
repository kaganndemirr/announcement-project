# Django
from django.http import JsonResponse
from django.conf import settings
from django.views.generic import View, TemplateView
from django.views.static import serve
from datetime import date
from datetime import timedelta

# Local
from departments.models import Announcement, Slide, Event
from classes.models import Lecture, Exam


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
            'domain_documentation': '/documentation/',
        })

        return context


class DocumentationView(View):

    def get(self, request, path='index.html', **kwargs):
        return serve(
            request, path, document_root=settings.DOCUMENTATION_ROOT, **kwargs
        )


class MainView(TemplateView):
    template_name = 'main.html'


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
                    .filter(department=request.user.department)
                    .order_by('-creation_time').values()
        ]
        return JsonResponse({"slides": list(data)})


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


class AjaxLectures(View):
    def get(self, request):
        data = [
            {
                'code': i['l_code'],
                'name': i['title'],
                'lecturer': i['lecturer'],
                'time': j.l_date.time(),
            }

            for j in Lecture
                    .objects
                    .filter(department=request.user.department,
                        l_date__date=date.today())
                    .order_by('l_date')

            for i in Lecture
                    .objects
                    .filter(department=request.user.department,
                        l_date__date=date.today())
                    .order_by('l_date').values()
        ]
        return JsonResponse({"lectures": list(data)})


class AjaxExams(View):
    def get(self, request):
        data = [
            {
                'code': j.lecture.l_code,
                'name': j.lecture.title,
                'lecturer': j.lecture.lecturer,
                'datetime': i['e_date'],
                'location': i['location'],
                'duration': i['duration']
            }

            for j in Exam
                    .objects
                    .filter(lecture__department=request.user.department,
                        e_date__date__gt=date.today())
                    .order_by('e_date')

            for i in Exam
                    .objects
                    .filter(lecture__department=request.user.department,
                        e_date__date=date.today())
                    .order_by('e_date').values()
        ]
        return JsonResponse({"exams": list(data)})


class AjaxEvents(View):
    def get(self, request):
        data = [
            {
                'date': i['date'],
                'name': i['name'],
                'location': i['location']
            }

            for i in Event
                    .objects
                    .filter(department=request.user.department,
                        date__date__gte=date.today())
                    .order_by('date').values()
        ]
        return JsonResponse({"events": list(data)})


class AjaxWeather(View):
    def get(self, request):
        # request.GET['param']
        data =  dict()
        data['Trabzon'] = 'Yağışlı'
        return JsonResponse(data)
