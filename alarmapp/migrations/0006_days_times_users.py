# Generated by Django 2.2.3 on 2019-10-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmapp', '0005_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='dayname')),
            ],
        ),
        migrations.CreateModel(
            name='times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeing', models.CharField(max_length=120, verbose_name='time')),
                ('timenum', models.CharField(max_length=120, verbose_name='time in numbers')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, verbose_name='Username')),
                ('pwd', models.CharField(max_length=120, verbose_name='Password')),
            ],
        ),
    ]
