# Generated by Django 3.1.4 on 2020-12-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='social_url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
