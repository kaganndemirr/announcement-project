from django.contrib import admin

# Local
from .models import Lecture, Exam


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    fields = ('department', 'l_code', 'title', 'lecturer', 'l_date')

    list_display = ('department', 'l_code', 'title', 'lecturer', 'l_date')

    def get_queryset(self, request):
        qs = super(LectureAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(department=request.user.department)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    fields = ('lecture', 'e_date', 'location', 'duration')

    list_display = ('lecture', 'e_date', 'location', 'duration')

    def get_queryset(self, request):
        qs = super(ExamAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(lecture__department=request.user.department)
