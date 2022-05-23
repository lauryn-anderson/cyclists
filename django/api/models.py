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
