# Generated by Django 2.1.7 on 2019-03-24 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0005_auto_20190323_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 20, 41, 9, 285177), verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='content',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 20, 41, 9, 285177), verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Video'), (1, 'Picture'), (2, 'Text')], verbose_name='Data Type'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 20, 41, 9, 285177), verbose_name='Date'),
        ),
    ]