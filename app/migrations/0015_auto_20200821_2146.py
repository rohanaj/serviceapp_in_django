# Generated by Django 2.1 on 2020-08-21 16:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200821_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 16, 16, 7, 300351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requestlist',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 16, 16, 7, 300351, tzinfo=utc)),
        ),
    ]
