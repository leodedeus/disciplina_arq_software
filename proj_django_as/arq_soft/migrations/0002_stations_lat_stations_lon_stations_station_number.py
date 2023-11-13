# Generated by Django 4.2.6 on 2023-11-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arq_soft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stations',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stations',
            name='station_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
