# Generated by Django 4.2.6 on 2023-11-07 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('total_hours', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': True,
            },
        ),
    ]
