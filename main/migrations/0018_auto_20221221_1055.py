# Generated by Django 3.2.9 on 2022-12-21 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_event_event_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_start_time',
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=30)),
                ('menu_is_vege', models.BooleanField(default=False)),
                ('menu_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('menu_drink', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.drink')),
                ('menu_food', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.food')),
            ],
        ),
    ]
