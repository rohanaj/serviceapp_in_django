# Generated by Django 2.1 on 2020-08-20 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200820_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlist',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
