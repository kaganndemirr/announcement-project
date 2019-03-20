from django.contrib import admin

# Local
from .models import Lecture, Exam


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    fields = ('l_code', 'title', 'lecturer', 'l_date')

    list_display = ('l_code', 'title', 'lecturer', 'l_date')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    fields = ('lecture', 'e_date', 'location', 'duration')

    list_display = ('lecture', 'e_date', 'location', 'duration')
