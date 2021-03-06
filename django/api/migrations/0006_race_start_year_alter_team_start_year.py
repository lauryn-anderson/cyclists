# Generated by Django 4.0.4 on 2022-05-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_discipline_team_remove_race_start_year_award_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='start_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Start Year'),
        ),
        migrations.AlterField(
            model_name='team',
            name='start_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
