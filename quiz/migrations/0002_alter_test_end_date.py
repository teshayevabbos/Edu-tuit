# Generated by Django 4.2 on 2023-05-22 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 30, 16, 13, 24, 291257, tzinfo=datetime.timezone.utc)),
        ),
    ]
