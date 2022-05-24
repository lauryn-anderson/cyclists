from rest_framework.routers import SimpleRouter
from .views import (
    PersonViewSet, RaceViewSet, EditionViewSet, StageViewSet, AwardViewSet,
    RaceParticipationViewSet, StageParticipationViewSet,
)


router = SimpleRouter()
router.register('person', PersonViewSet, basename='person')
router.register('race', RaceViewSet, basename='race')
router.register('edition', EditionViewSet, basename='edition')
router.register('stage', StageViewSet, basename='stage')
router.register('award', AwardViewSet, basename='award')
router.register('participation', RaceParticipationViewSet, basename='participation')
router.register('stage_participation', StageParticipationViewSet, basename='stage_participation')

urlpatterns = router.urls
