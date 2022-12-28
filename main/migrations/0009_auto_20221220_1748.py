# Generated by Django 3.2.9 on 2022-12-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20221220_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='host_event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_host',
        ),
        migrations.AddField(
            model_name='event',
            name='event_host',
            field=models.ManyToManyField(to='main.Host'),
        ),
    ]