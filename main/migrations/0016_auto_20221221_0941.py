# Generated by Django 3.2.9 on 2022-12-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20221221_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='drink_amount',
            field=models.DecimalField(decimal_places=2, default='0.03', max_digits=6),
        ),
        migrations.AlterField(
            model_name='drink',
            name='drink_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_name',
            field=models.CharField(max_length=30),
        ),
    ]