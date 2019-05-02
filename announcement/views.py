# Django
from django.http import JsonResponse
from django.conf import settings
from django.views.generic import View, TemplateView
from django.views.static import serve
from datetime import date
from datetime import timedelta

# Local
from departments.models import Announcement, Content, Event
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


class AjaxContents(View):
    def get(self, request):
        data = Content.objects.filter(department=request.user.department,
            status=0).order_by('creation_time').values()
        return JsonResponse({"contents": list(data)})


class AjaxAnnouncement(View):
    def get(self, request):
        data = Announcement.objects.filter(department=request.user.department).values()
        return JsonResponse({"announcements": list(data)})


class AjaxLectures(View):
    def get(self, request):
        data = Lecture.objects.filter(department=request.user.department,
            l_date__date=date.today() + timedelta(days=1)).order_by('l_date').values()
        return JsonResponse({"lectures": list(data)})

class AjaxExams(View):
    def get(self, request):
        data = Exam.objects.filter(lecture__department=request.user.department,
            e_date__date=date.today() + timedelta(days=1)).order_by('e_date').values()
        return JsonResponse({"exams": list(data)})

class AjaxEvents(View):
    def get(self, request):
        data = Event.objects.filter(department=request.user.department,
            date__date=date.today() + timedelta(days=1)).order_by('date').values()
        return JsonResponse({"events": list(data)})

class AjaxWeather(View):
    def get(self, request):
        # request.GET['param']
        data =  dict()
        data['Trabzon'] = 'Yağışlı'
        return JsonResponse(data)
