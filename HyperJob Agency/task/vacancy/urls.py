from django.urls import path
from . import views

urlpatterns = [
    path('', views.Vacancy.as_view()),
    path('new', views.NewVacancy.as_view())
]

