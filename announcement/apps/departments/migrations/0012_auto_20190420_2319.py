# Generated by Django 2.1.7 on 2019-04-20 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0011_auto_20190420_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 23, 19, 33, 823664), verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='content',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 23, 19, 33, 822665), verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 23, 19, 33, 823664), verbose_name='Date'),
        ),
    ]
