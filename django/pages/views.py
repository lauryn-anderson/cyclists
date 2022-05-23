from django.views.generic import TemplateView, ListView, DetailView

from api.models import Person


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
