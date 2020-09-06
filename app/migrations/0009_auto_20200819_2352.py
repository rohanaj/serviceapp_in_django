# Generated by Django 2.1 on 2020-08-19 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200819_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestlist',
            name='requesttype',
        ),
        migrations.AddField(
            model_name='requestlist',
            name='requesttype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.RequestType'),
        ),
    ]