from rest_framework import viewsets
from .models import (
    Person, Race, Edition, Stage, Award, RaceParticipation, StageParticipation,
)
from .serializers import (
    PersonSerializer, RaceSerializer, EditionSerializer, StageSerializer,
    AwardSerializer, RaceParticipationSerializer, StageParticipationSerializer,
)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class EditionViewSet(viewsets.ModelViewSet):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class RaceParticipationViewSet(viewsets.ModelViewSet):
    queryset = RaceParticipation.objects.all()
    serializer_class = RaceParticipationSerializer


class StageParticipationViewSet(viewsets.ModelViewSet):
    queryset = StageParticipation.objects.all()
    serializer_class = StageParticipationSerializer

