# Generated by Django 3.2.9 on 2022-12-21 13:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20221221_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_food',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.food'),
        ),
    ]
