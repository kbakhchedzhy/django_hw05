# Generated by Django 3.1.4 on 2021-01-13 18:56
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210111_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL,
                related_name='subject_of_student', to='home.subject'),
        ),
    ]