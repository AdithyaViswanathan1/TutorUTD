# Generated by Django 4.2.5 on 2023-11-08 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite_Tutors_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student',
            new_name='student_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='total_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Favorite_Tutors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.tutor')),
            ],
            options={
                'db_table': 'favorite_tutors',
                'managed': True,
            },
        ),
    ]