# Generated by Django 3.1.2 on 2021-01-21 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_project1_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project1',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 10, 51, 46, 582272)),
        ),
    ]
