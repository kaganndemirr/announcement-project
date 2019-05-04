# Generated by Django 2.1.7 on 2019-05-03 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0015_auto_20190503_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='data',
            field=models.TextField(max_length=500, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Video'), (1, 'Picture'), (2, 'Text')], verbose_name='Content Type'),
        ),
    ]
