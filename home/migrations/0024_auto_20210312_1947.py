# Generated by Django 3.1.5 on 2021-03-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210312_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
