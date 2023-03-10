# Generated by Django 3.2.9 on 2022-12-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_host', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(verbose_name='date')),
                ('place', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
