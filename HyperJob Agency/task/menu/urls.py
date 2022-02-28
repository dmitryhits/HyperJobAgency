from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.main_menu),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('signup', views.HyperJobSignupView.as_view()),
    path('login', views.HyperJobLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('home', views.CreateProfile.as_view()),
    # path('resume/new', views.NewResume.as_view()),
    # path('vacancy/new', views.NewVacancy.as_view()),
]
