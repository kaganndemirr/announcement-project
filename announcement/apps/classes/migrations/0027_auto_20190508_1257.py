# Generated by Django 2.1.7 on 2019-05-08 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0026_auto_20190505_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='location',
            field=models.CharField(blank=True, max_length=100, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecturer',
            field=models.CharField(max_length=60, verbose_name='Lecturer Name'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Lecture Name'),
        ),
    ]