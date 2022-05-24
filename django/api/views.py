from rest_framework import viewsets
from .models import (
    Person, Race, Edition, Stage, Award, RaceParticipation, StageParticipation,
    Team, TeamName, Discipline, Contract,
)
from .serializers import (
    PersonSerializer, RaceSerializer, EditionSerializer, StageSerializer,
    AwardSerializer, RaceParticipationSerializer, StageParticipationSerializer,
    TeamSerializer, TeamNameSerializer, DisciplineSerializer, ContractSerializer,
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


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamNameViewSet(viewsets.ModelViewSet):
    queryset = TeamName.objects.all()
    serializer_class = TeamNameSerializer


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
