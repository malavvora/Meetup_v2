# Generated by Django 2.0.5 on 2018-06-12 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0026_remove_meetup_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='created_by',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='meetup.User'),
        ),
    ]