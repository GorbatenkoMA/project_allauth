from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):

    template_name = 'allauth_app/home.html'
