# Generated by Django 3.1.4 on 2021-01-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210114_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(to='home.Teacher'),
        ),
    ]
