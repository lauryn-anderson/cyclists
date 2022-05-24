from django.urls import path
from .views import (
    HomePageView, PersonDetailView, PersonListView, RaceListView,
    RaceDetailView, EditionDetailView, StageDetailView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('people/', PersonListView.as_view(), name='people'),
    path('<uuid:pk>/', PersonDetailView.as_view(), name='person'),
    path('races/', RaceListView.as_view(), name='races'),
    path('races/<uuid:pk>/', RaceDetailView.as_view(), name='race'),
    path('editions/<uuid:pk>/', EditionDetailView.as_view(), name='edition'),
    path('stages/<uuid:pk>/', StageDetailView.as_view(), name='stage'),
]
