from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from django import forms


def main_menu(request):
    return render(request, 'menu/index.html')


class HyperJobSignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'menu/signup.html'


class HyperJobLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'menu/login.html'


class ResumeForm(forms.Form):
    description = forms.CharField(max_length=2048, label='Resume Description')


class VacancyForm(forms.Form):
    description = forms.CharField(max_length=2048, label='Vacancy Description')


class CreateProfile(View):

    def get(self, request):
        form = {}
        if request.user.is_authenticated:
            if request.user.is_staff:
                form['username'] = request.user.username
                form['vacancy'] = VacancyForm()
            else:
                form['username'] = request.user.username
                form['resume'] = ResumeForm()
        return render(request, 'menu/profile.html', {'form': form})




