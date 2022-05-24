# Generated by Django 4.0.4 on 2022-05-24 00:58

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_award_edition_race_raceparticipation_stage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=15, verbose_name='Abbreviation')),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('notes', models.TextField(blank=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('strava', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
                ('start_year', models.PositiveSmallIntegerField(blank=True)),
                ('disciplines', models.ManyToManyField(related_name='teams', to='api.discipline')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='race',
            name='start_year',
        ),
        migrations.AddField(
            model_name='award',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='edition',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='race',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='raceparticipation',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='stage',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='number',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Stage Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stageparticipation',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='award',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='edition',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='strava',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='race',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name='TeamName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
                ('nicknames', models.CharField(max_length=200, verbose_name='Nickname(s)')),
                ('notes', models.TextField(blank=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='api.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('notes', models.TextField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='disciplines',
            field=models.ManyToManyField(related_name='people', to='api.discipline'),
        ),
        migrations.AddField(
            model_name='person',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='members', through='api.Contract', to='api.team'),
        ),
        migrations.AddField(
            model_name='raceparticipation',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.team'),
        ),
        migrations.AlterField(
            model_name='race',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='races', to='api.discipline'),
        ),
    ]