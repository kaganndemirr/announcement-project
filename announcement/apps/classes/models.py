# Standart Library
from datetime import datetime

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Lecture(models.Model):
    department = models.ForeignKey(
        verbose_name=_('Department'), to='departments.Department',
        on_delete=models.CASCADE, null=True, blank=True, editable=False
    )
    l_code = models.CharField(verbose_name='Code', max_length=10, unique=True)
    title = models.CharField(verbose_name='Lecture Name', max_length=30)
    lecturer = models.CharField(verbose_name='Lecturer Name', max_length=30)
    l_date = models.DateTimeField(verbose_name=_('Lecture Date '), default=datetime.now())

    class Meta:
        verbose_name = _('Lecture')
        verbose_name_plural = _('Lectures')

    def __str__(self):
        return '{title}'.format(title=self.title)


class Exam(models.Model):
    lecture = models.ForeignKey(to='classes.Lecture', on_delete=models.CASCADE)
    e_date = models.DateTimeField(verbose_name=_('Exam Date'), default=datetime.now())
    duration = models.CharField(verbose_name='Duration', max_length=10)
    location = models.CharField(verbose_name='Location', max_length=50, blank=True)

    class Meta:
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')

    def __str__(self):
        return '{lecture}'.format(lecture=self.lecture.title)
