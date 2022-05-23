from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Person


class PersonSerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id', 'full_name', 'preferred_name', 'nicknames',
            'birthdate', 'nationality', 'instagram', 'twitter',
            'strava',
        )
