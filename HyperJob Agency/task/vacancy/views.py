from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
# Create your views here.

# bart = User.objects.create_user('bart')
# vacancy = models.Vacancy.objects.create(description='Job', author=bart)

class Vacancy(View):
    vacancies = models.Vacancy.objects.all()

    def get(self, request, *args, **kwargs):
        for vacancy in self.vacancies:
            print('Vacancies:', vacancy.author.username, vacancy.description)
        return render(request, 'vacancy/vacancy.html', {'vacancies': self.vacancies})

class NewVacancy(View):

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponse(status=403)
        else:
            if request.user.is_staff:
                description = request.POST.get('description')
                print(request.user.username, description)
                new_vacancy = models.Vacancy.objects.create(description=description, author=request.user)
                return redirect('/home')
            else:
                return HttpResponse(status=403)
