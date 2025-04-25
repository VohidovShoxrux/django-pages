from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class InfoPageView(TemplateView):
    template_name = 'info.html'

class AdditiomPageView(TemplateView):
    template_name = 'addition.html'

class IndexPageView(TemplateView):
    template_name = 'index.html'