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


class Outcomes(models.TextChoices):
    FIN = 'FIN', 'FIN'
    DNS = 'DNS', 'DNS'
    DNF = 'DNF', 'DNF'
    DSQ = 'DSQ', 'DSQ'


class Discipline(BaseModel):

    name = models.CharField(max_length=100)
    abbreviation = models.CharField('Abbreviation', max_length=15)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Race(BaseModel):

    name = models.CharField(max_length=100)
    nicknames = models.CharField('Nickname(s)', max_length=200, blank=True)
    pronunciation = models.CharField(max_length=100, blank=True)
    start_year = models.PositiveSmallIntegerField('Start Year', null=True, blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    country = CountryField(blank=True)
    discipline = models.ForeignKey(
        Discipline, related_name='races', on_delete=models.SET_NULL, null=True)

    def age(self):
        return get_age(self.start_year)

    def __str__(self):
        return self.name


class Edition(BaseModel):

    race = models.ForeignKey(Race, related_name='editions', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField('Year')
    start_date = models.DateField('Start Date', null=True, blank=True)
    end_date = models.DateField('End Date', null=True, blank=True)
    start_location = models.CharField('Start Location', max_length=200, blank=True)
    end_location = models.CharField('End Location', max_length=200, blank=True)
    distance = models.FloatField('Distance (km)', blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.year) + ' ' + self.race.__str__()


class Stage(BaseModel):

    edition = models.ForeignKey(Edition, related_name='stages', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField('Stage Number')
    date = models.DateField('Start Date', null=True, blank=True)
    start_location = models.CharField('Start Location', max_length=200, blank=True)
    end_location = models.CharField('End Location', max_length=200, blank=True)
    distance = models.FloatField('Distance (km)', blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return 'Stage ' + str(self.number) + ' of the ' + self.edition.__str__()


class Award(BaseModel):

    name = models.CharField(max_length=100)
    race = models.ForeignKey(
        Race, related_name='awards', on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Team(BaseModel):

    notes = models.TextField(blank=True)
    country = CountryField(blank=True)
    disciplines = models.ManyToManyField(Discipline, related_name='teams')
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    strava = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    start_year = models.PositiveSmallIntegerField(null=True, blank=True)

    def name(self):
        return TeamName.objects.filter(team=self).order_by('-start_date').first()

    def age(self):
        return get_age(self.start_year)

    def __str__(self):
        self.name().__str__()


class TeamName(BaseModel):

    team = models.ForeignKey(Team, related_name='names', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    nicknames = models.CharField('Nickname(s)', max_length=200)
    notes = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Person(BaseModel):

    full_name = models.CharField('Full Name', max_length=100, blank=True)
    preferred_name = models.CharField('Preferred Name', max_length=100)
    pronunciation = models.CharField(max_length=100, blank=True)
    nicknames = models.CharField('Nickname(s)', max_length=200, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    nationality = CountryField(null=True, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    strava = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    disciplines = models.ManyToManyField(Discipline, related_name='people')

    def __str__(self):
        return self.preferred_name

    def age(self):
        return get_age(self.birthdate)

    races = models.ManyToManyField(
        Edition,
        related_name='riders',
        through='RaceParticipation',
        blank=True,
    )
    teams = models.ManyToManyField(
        Team,
        related_name='members',
        through='Contract',
        blank=True,
    )


class RaceParticipation(BaseModel):

    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    rider = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Position', blank=True)
    number = models.PositiveIntegerField('Jersey Number', blank=True)
    awards = models.ManyToManyField(Award, related_name='wins', blank=True)
    notes = models.TextField('Notes', blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
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
    notes = models.TextField('Notes', blank=True)

    outcome = models.CharField(
        'Outcome',
        max_length=3,
        choices=Outcomes.choices,
        default=Outcomes.FIN,
    )
    outcome_notes = models.TextField('Outcome_notes', blank=True)


class Contract(BaseModel):
    
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField('Start Date', null=True, blank=True)
    end_date = models.DateField('End Date', null=True, blank=True)
    notes = models.TextField(blank=True)


def get_age(birthdate):
    if birthdate is not None:
        today = datetime.date.today()
        if hasattr(birthdate, 'year'):
            # datetime
            years = today.year - birthdate.year
            if today.month > birthdate.month:
                # birthday has happened this year
                return years
            if today.month < birthdate.month:
                # birthday has not happened yet
                return years - 1
            if today.day >= birthdate.day:
                # birthday has happened/is today
                return years
            else:
                # birthday has not happened yet
                return years - 1
        else:
            # integer (year)
            return today.year - birthdate.year
