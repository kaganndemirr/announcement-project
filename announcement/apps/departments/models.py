# Standart Library
from datetime import datetime

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local
from .variables import SITUATIONS, TYPES


class Department(models.Model):
    d_code = models.CharField(verbose_name='Department Code', max_length=10, unique=True)
    name = models.CharField(verbose_name='Department Name', max_length=60)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return '{name}'.format(name=self.name)


class Slide(models.Model):
    department = models.ForeignKey(
        verbose_name='Department', to='departments.Department',
        on_delete=models.CASCADE, null=True, blank=True, editable=False
    )
    title = models.CharField(verbose_name='Title', max_length=100)
    status = models.SmallIntegerField(verbose_name='Status', choices=SITUATIONS)
    creation_time = models.DateTimeField(verbose_name=_('Creation Time'), default=datetime.now)
    data = models.TextField(verbose_name='Content', max_length=500)
    type = models.SmallIntegerField(verbose_name='Content Type', choices=TYPES)

    class Meta:
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')

    def __str__(self):
        return '{title}'.format(title=self.title)


class Event(models.Model):
    department = models.ForeignKey(
        verbose_name='Department', to='departments.Department',
        on_delete=models.CASCADE, null=True, blank=True, editable=False
    )
    date = models.DateTimeField(verbose_name=_('Date'), default=datetime.now)
    location = models.CharField(verbose_name='Location', max_length=100)
    name = models.CharField(verbose_name='Name', max_length=150)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return '{name}'.format(name=self.name)


class Announcement(models.Model):
    department = models.ForeignKey(
        verbose_name='Department', to='departments.Department',
        on_delete=models.CASCADE, null=True, blank=True, editable=False
    )
    creation_date = models.DateTimeField(verbose_name=_('Creation Time'), default=datetime.now)
    title = models.CharField(verbose_name='Title', max_length=150)

    class Meta:
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')

    def __str__(self):
        return '{title}'.format(title=self.title)
