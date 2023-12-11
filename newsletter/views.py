from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from newsletter.models import Client


class IndexView(TemplateView):
    template_name = 'newsletter/index.html'


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'comment')
    success_url = reverse_lazy('newsletter:clients')


class ClientDetailView(DetailView):
    model = Client
