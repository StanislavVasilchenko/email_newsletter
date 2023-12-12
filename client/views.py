from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from client.models import Client


class IndexView(TemplateView):
    template_name = 'client/index.html'
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        count = Client.objects.count()
        context_data['count'] = count
        return context_data


class ClientListView(ListView):
    model = Client

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data()
    #     count = 0
    #     context_data['count'] = count + 1
    #     return context_data


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'comment',)
    success_url = reverse_lazy('client:clients')


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'comment',)

    def get_success_url(self):
        return reverse('client:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:clients')
