# Generated by Django 2.0.5 on 2018-06-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0012_remove_meetup_meetup_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_date',
            field=models.DateTimeField(verbose_name='date of meetup'),
        ),
    ]
