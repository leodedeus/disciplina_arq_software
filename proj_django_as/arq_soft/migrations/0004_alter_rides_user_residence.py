# Generated by Django 4.2.6 on 2023-11-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arq_soft', '0003_rides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='user_residence',
            field=models.CharField(max_length=200),
        ),
    ]
