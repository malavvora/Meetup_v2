# Generated by Django 2.0.5 on 2018-06-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0010_auto_20180611_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_time',
            field=models.TimeField(blank=True, verbose_name='time of meetup'),
        ),
    ]
