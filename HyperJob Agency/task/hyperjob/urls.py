"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('menu.urls')),
    path('resume/', include('resume.urls')),
    path('resumes/', RedirectView.as_view(url='/resumes')),
    path('resumes', include('resume.urls')),
    path('vacancy/', include('vacancy.urls')),
    path('vacancies/', RedirectView.as_view(url='/vacancies')),
    path('vacancies', include('vacancy.urls')),
    path('admin/', admin.site.urls),
]
