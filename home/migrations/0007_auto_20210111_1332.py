# Generated by Django 3.1.4 on 2021-01-11 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210111_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title_of_book',
            new_name='title',
        ),
    ]