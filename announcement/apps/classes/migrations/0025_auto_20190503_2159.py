# Generated by Django 2.1.7 on 2019-05-03 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0024_auto_20190503_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='e_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Exam Date'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='l_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Lecture Date '),
        ),
    ]