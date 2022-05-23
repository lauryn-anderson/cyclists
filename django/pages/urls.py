from django.urls import path
from .views import HomePageView, PersonDetailView, PersonListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('people/', PersonListView.as_view(), name='people'),
    path('<uuid:pk>/', PersonDetailView.as_view(), name='person'),
]
