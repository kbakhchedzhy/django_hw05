# Generated by Django 3.1.4 on 2021-01-14 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210114_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='students',
            new_name='student',
        ),
    ]
