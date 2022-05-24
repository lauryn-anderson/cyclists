from rest_framework.routers import SimpleRouter
from .views import (
    PersonViewSet, RaceViewSet, EditionViewSet, StageViewSet, AwardViewSet,
    RaceParticipationViewSet, StageParticipationViewSet, TeamViewSet,
    TeamNameViewSet, ContractViewSet, DisciplineViewSet,
)


router = SimpleRouter()
router.register('person', PersonViewSet, basename='person')
router.register('race', RaceViewSet, basename='race')
router.register('edition', EditionViewSet, basename='edition')
router.register('stage', StageViewSet, basename='stage')
router.register('award', AwardViewSet, basename='award')
router.register('participation', RaceParticipationViewSet, basename='participation')
router.register('stage_participation', StageParticipationViewSet, basename='stage_participation')
router.register('team', TeamViewSet, basename='team')
router.register('team_name', TeamNameViewSet, basename='team_name')
router.register('contract', ContractViewSet, basename='contract')
router.register('discipline', DisciplineViewSet, basename='discipline')

urlpatterns = router.urls
