from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from . import models

# homer = models.User.objects.create_user("Homer")
# bart_resume = models.objects.create(description="Job", author=homer)


class Resume(TemplateView):
    # resumes = models.Resume.objects.all()
    template_name = 'resume/resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['resumes'] = models.Resume.objects.all()
        return context

    # def get(self, request, *args, **kwargs):
    #     print('ALL RESUMES:')
    #     for resume in self.resumes:
    #         print('Resumes:', resume.author.username, resume.description)
    #     return render(request, 'resume/resume.html', {'resumes': self.resumes})


class NewResume(View):
    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponse(status=403)
        else:
            description = request.POST.get('description')
            print('NEW RESUME:', request.user.username, description)
            new_resume = models.Resume.objects.create(description=description, author=request.user)
            print('NEW RESUME created:', new_resume.author.username, new_resume.description)
            for resume in models.Resume.objects.all():
                print('Resumes retrieved:', resume.author.username, resume.description)
            # new_resume.save()
            return redirect('/home')




