# Generated by Django 2.1.7 on 2019-04-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190420_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.IntegerField(blank=True, unique=True, verbose_name='Student ID'),
        ),
    ]