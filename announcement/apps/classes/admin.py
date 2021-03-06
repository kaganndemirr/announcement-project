from django.contrib import admin

# Local
from .models import Lecture, Exam, LectureSession


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    fields = ('l_code', 'title', 'lecturer')

    list_display = ('department', 'l_code', 'title', 'lecturer')

    def get_queryset(self, request):
        qs = super(LectureAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(department=request.user.department)

    def save_model(self, request, obj, form, change):
        obj.department = request.user.department
        super().save_model(request, obj, form, change)

@admin.register(LectureSession)
class LectureSessionAdmin(admin.ModelAdmin):
    fields = ('lecture', 's_date', 'location', 'duration')

    list_display = ('lecture', 's_date', 'location', 'duration')

    def get_queryset(self, request):
        qs = super(LectureSessionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(lecture__department=request.user.department)

    def get_form(self, request, obj=None, **kwargs):
        form = super(LectureSessionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['lecture']._queryset = Lecture.objects.filter(department=request.user.department)
        return form

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    fields = ('lecture', 'e_date', 'location', 'duration')

    list_display = ('lecture', 'e_date', 'location', 'duration')

    def get_queryset(self, request):
        qs = super(ExamAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(lecture__department=request.user.department)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ExamAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['lecture']._queryset = Lecture.objects.filter(department=request.user.department)
        return form
