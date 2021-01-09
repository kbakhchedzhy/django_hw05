# Generated by Django 3.1.4 on 2021-01-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201224_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='normalized_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='social_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
