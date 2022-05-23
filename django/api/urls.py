from django.urls import path
from .views import PersonList, PersonDetail

urlpatterns = [
    path('', PersonList.as_view()),
    path('<uuid:pk>/', PersonDetail.as_view()),
]
