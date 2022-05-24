from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import (
    Person, Race, Edition, Stage, Award, RaceParticipation, StageParticipation,
)


class PersonSerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id', 'full_name', 'preferred_name', 'nicknames',
            'birthdate', 'nationality', 'instagram', 'twitter',
            'strava',
        )


class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = (
            'id', 'name', 'nicknames', 'start_year', 'website', 'discipline',
        )


class EditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Edition
        fields = (
            'id', 'race', 'year', 'start_date', 'end_date', 'start_location',
            'end_location', 'distance',
        )


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = (
            'id', 'edition', 'date', 'start_location', 'end_location', 'distance',
        )


class AwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Award
        fields = (
            'id', 'name', 'race',
        )


class RaceParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaceParticipation
        fields = (
            'id', 'edition', 'rider', 'position', 'number', 'awards', 'outcome',
            'outcome_notes',
        )


class StageParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StageParticipation
        fields = (
            'id', 'stage', 'race_participation', 'position', 'awards', 'outcome',
            'outcome_notes',
        )

