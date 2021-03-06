# Generated by Django 4.0.4 on 2022-05-23 23:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_person_instagram_person_strava_person_twitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('start_date', models.DateField(blank=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, verbose_name='End Date')),
                ('start_location', models.CharField(blank=True, max_length=200, verbose_name='Start Location')),
                ('end_location', models.CharField(blank=True, max_length=200, verbose_name='End Location')),
                ('distance', models.FloatField(blank=True, verbose_name='Distance (km)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('nicknames', models.CharField(max_length=200, verbose_name='Nickname(s)')),
                ('start_year', models.DateField(blank=True, verbose_name='Start Year')),
                ('website', models.URLField(blank=True, verbose_name='Website')),
                ('discipline', models.CharField(blank=True, choices=[('ROAD', 'Road'), ('CROSS', 'Cyclo-cross'), ('MOUNTAIN', 'Mountain'), ('TRACK', 'Track'), ('BMX', 'BMX')], max_length=10, verbose_name='Discipline')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RaceParticipation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.PositiveIntegerField(blank=True, verbose_name='Position')),
                ('number', models.PositiveIntegerField(blank=True, verbose_name='Jersey Number')),
                ('outcome', models.CharField(choices=[('FIN', 'FIN'), ('DNS', 'DNS'), ('DNF', 'DNF'), ('DSQ', 'DSQ')], default='FIN', max_length=3, verbose_name='Outcome')),
                ('outcome_notes', models.TextField(blank=True, verbose_name='Outcome_notes')),
                ('awards', models.ManyToManyField(blank=True, related_name='wins', to='api.award')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.edition')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, verbose_name='Start Date')),
                ('start_location', models.CharField(blank=True, max_length=200, verbose_name='Start Location')),
                ('end_location', models.CharField(blank=True, max_length=200, verbose_name='End Location')),
                ('distance', models.FloatField(blank=True, verbose_name='Distance (km)')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='api.edition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StageParticipation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.PositiveIntegerField(blank=True, verbose_name='Position')),
                ('outcome', models.CharField(choices=[('FIN', 'FIN'), ('DNS', 'DNS'), ('DNF', 'DNF'), ('DSQ', 'DSQ')], default='FIN', max_length=3, verbose_name='Outcome')),
                ('outcome_notes', models.TextField(blank=True, verbose_name='Outcome_notes')),
                ('awards', models.ManyToManyField(blank=True, related_name='stage_wins', to='api.award')),
                ('race_participation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='api.raceparticipation')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='edition',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editions', to='api.race'),
        ),
        migrations.AddField(
            model_name='award',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='api.race'),
        ),
        migrations.AddField(
            model_name='person',
            name='races',
            field=models.ManyToManyField(blank=True, related_name='riders', through='api.RaceParticipation', to='api.edition'),
        ),
    ]
