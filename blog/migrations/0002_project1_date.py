# Generated by Django 3.1.2 on 2021-01-21 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project1',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 10, 43, 38, 599055)),
        ),
    ]
