# Generated by Django 3.2.9 on 2022-12-21 12:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20221221_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]