# Generated by Django 5.0.3 on 2024-03-09 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='data_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 9, 13, 2, 28, 69085, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
