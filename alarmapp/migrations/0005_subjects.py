# Generated by Django 2.2.3 on 2019-10-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmapp', '0004_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, verbose_name='username')),
                ('subject', models.CharField(max_length=120, verbose_name='subject_name')),
            ],
        ),
    ]
