from django.views.generic import TemplateView, ListView, DetailView

from api.models import Person, Race, Edition, Stage


class HomePageView(TemplateView):
    template_name = 'home.html'


class PersonListView(ListView):
    model = Person
    template_name = 'people.html'
    context_object_name = 'people'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'person.html'
    context_object_name = 'person'


class RaceListView(ListView):
    model = Race
    template_name = 'races.html'
    context_object_name = 'races'


class RaceDetailView(DetailView):
    model = Race
    template_name = 'race.html'
    context_object_name = 'race'


class EditionDetailView(DetailView):
    model = Edition
    template_name = 'edition.html'
    context_object_name = 'edition'


class StageDetailView(DetailView):
    model = Stage
    template_name = 'stage.html'
    context_object_name = 'stage'

