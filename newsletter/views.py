from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from newsletter.models import Client


class IndexView(TemplateView):
    template_name = 'newsletter/index.html'


class ClientListView(ListView):
    model = Client
