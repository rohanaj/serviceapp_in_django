# Generated by Django 2.1 on 2020-08-18 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200818_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlist',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]