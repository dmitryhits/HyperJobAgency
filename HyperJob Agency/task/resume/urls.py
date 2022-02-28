from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.Resume.as_view()),
    path('new/', RedirectView.as_view(url='/new')),
    path('new', views.NewResume.as_view()),
]
