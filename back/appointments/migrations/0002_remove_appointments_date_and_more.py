# Generated by Django 4.2.5 on 2023-11-10 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='start_time',
        ),
        migrations.AddField(
            model_name='appointments',
            name='course',
            field=models.CharField(default='None', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
    ]
