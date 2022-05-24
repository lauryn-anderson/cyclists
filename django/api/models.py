import datetime

from django.db import models
from django_countries.fields import CountryField

import uuid


class BaseModel(models.Model):
    """
    Abstract base class that provides a blueprint for all models.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class Race(BaseModel):

    name = models.CharField('Name', max_length=100)
    nicknames = models.CharField('Nickname(s)', max_length=200)
    start_year = models.DateField('Start Year', blank=True)
    website = models.URLField('Website', blank=True)

    class Disciplines(models.TextChoices):
        ROAD = 'ROAD', 'Road'
        CROSS = 'CROSS', 'Cyclo-cross'
        MOUNTAIN = 'MOUNTAIN', 'Mountain'
        TRACK = 'TRACK', 'Track'
        BMX = 'BMX', 'BMX'

    discipline = models.CharField(
        'Discipline',
        max_length=10,
        choices=Disciplines.choices,
        blank=True,
    )


class Edition(BaseModel):

    race = models.ForeignKey(Race, related_name='editions', on_delete=models.CASCADE)
    year = models.PositiveIntegerField('Year')
    start_date = models.DateField('Start Date', blank=True)
    end_date = models.DateField('End Date', blank=True)
    start_location = models.CharField('Start Location', max_length=200, blank=True)
    end_location = models.CharField('End Location', max_length=200, blank=True)
    distance = models.FloatField('Distance (km)', blank=True)


class Stage(BaseModel):

    edition = models.ForeignKey(Edition, related_name='stages', on_delete=models.CASCADE)
    date = models.DateField('Start Date', blank=True)
    start_location = models.CharField('Start Location', max_length=200, blank=True)
    end_location = models.CharField('End Location', max_length=200, blank=True)
    distance = models.FloatField('Distance (km)', blank=True)


class Award(BaseModel):

    name = models.CharField('Name', max_length=100)
    race = models.ForeignKey(
        Race, related_name='awards', on_delete=models.CASCADE, blank=True, null=True)


class Person(BaseModel):

    full_name = models.CharField('Full Name', max_length=100, blank=True)
    preferred_name = models.CharField('Preferred Name', max_length=100)
    nicknames = models.CharField('Nickname(s)', max_length=200, blank=True)
    birthdate = models.DateField('Birthdate', null=True, blank=True)
    nationality = CountryField(null=True, blank=True)
    instagram = models.CharField('Instagram', max_length=100, blank=True)
    twitter = models.CharField('Twitter', max_length=100, blank=True)
    strava = models.CharField('Strava', max_length=100, blank=True)

    def __str__(self):
        return self.preferred_name

    def age(self):
        if self.birthdate is not None:
            today = datetime.date.today()
            years = today.year - self.birthdate.year
            if today.month > self.birthdate.month:
                # birthday has happened this year
                return years
            if today.month < self.birthdate.month:
                # birthday has not happened yet
                return years - 1
            if today.day >= self.birthdate.day:
                # birthday has happened/is today
                return years
            else:
                # birthday has not happened yet
                return years - 1

    races = models.ManyToManyField(
        Edition,
        related_name='riders',
        through='RaceParticipation',
        blank=True,
    )


class Outcomes(models.TextChoices):
    FIN = 'FIN', 'FIN'
    DNS = 'DNS', 'DNS'
    DNF = 'DNF', 'DNF'
    DSQ = 'DSQ', 'DSQ'


class RaceParticipation(BaseModel):

    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    rider = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Position', blank=True)
    number = models.PositiveIntegerField('Jersey Number', blank=True)
    awards = models.ManyToManyField(Award, related_name='wins', blank=True)

    outcome = models.CharField(
        'Outcome',
        max_length=3,
        choices=Outcomes.choices,
        default=Outcomes.FIN,
    )
    outcome_notes = models.TextField('Outcome_notes', blank=True)


class StageParticipation(BaseModel):

    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    race_participation = models.ForeignKey(
        RaceParticipation, related_name='stages', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Position', blank=True)
    awards = models.ManyToManyField(Award, related_name='stage_wins', blank=True)

    outcome = models.CharField(
        'Outcome',
        max_length=3,
        choices=Outcomes.choices,
        default=Outcomes.FIN,
    )
    outcome_notes = models.TextField('Outcome_notes', blank=True)
