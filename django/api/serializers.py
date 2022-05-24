from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import (
    Person, Race, Edition, Stage, Award, RaceParticipation, StageParticipation,
    Team, TeamName, Discipline, Contract,
)


class PersonSerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id', 'full_name', 'preferred_name', 'nicknames',
            'birthdate', 'nationality', 'instagram', 'twitter',
            'strava', 'disciplines', 'notes', 'races', 'teams',
        )


class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = (
            'id', 'name', 'nicknames', 'start_year', 'website', 'discipline',
            'notes',
        )


class EditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Edition
        fields = (
            'id', 'race', 'year', 'start_date', 'end_date', 'start_location',
            'end_location', 'distance', 'notes',
        )


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = (
            'id', 'number', 'edition', 'date', 'start_location', 'end_location',
            'distance', 'notes',
        )


class AwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Award
        fields = (
            'id', 'name', 'race', 'notes',
        )


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = (
            'id', 'notes', 'country', 'disciplines', 'instagram', 'twitter',
            'strava', 'website', 'start_year',
        )


class TeamNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamName
        fields = (
            'id', 'team', 'name', 'abbreviation', 'notes', 'start_date',
            'end_date', 'nicknames',
        )


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = (
            'id', 'person', 'team', 'start_date', 'end_date', 'notes',
        )


class RaceParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaceParticipation
        fields = (
            'id', 'edition', 'rider', 'position', 'number', 'awards', 'outcome',
            'outcome_notes', 'team', 'notes',
        )


class StageParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StageParticipation
        fields = (
            'id', 'stage', 'race_participation', 'position', 'awards', 'outcome',
            'outcome_notes', 'notes',
        )


class DisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline
        fields = (
            'id', 'name', 'abbreviation', 'notes',
        )


