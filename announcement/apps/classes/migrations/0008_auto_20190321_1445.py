# Generated by Django 2.1.7 on 2019-03-21 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_auto_20190321_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='e_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 14, 45, 14, 898659), verbose_name='Exam Date'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='l_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 14, 45, 14, 898659), verbose_name='Lecture Date '),
        ),
    ]
