# Generated by Django 2.0.5 on 2018-06-12 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0020_auto_20180612_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetup_date', models.DateTimeField(verbose_name='date of meetup')),
                ('meetup_place', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-meetup_date'],
            },
        ),
        migrations.RemoveField(
            model_name='meetupgroups',
            name='group_category',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_description',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='MeetupGroups',
        ),
        migrations.AddField(
            model_name='meetup',
            name='meetup_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetup.Group'),
        ),
    ]