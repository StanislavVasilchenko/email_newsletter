from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from newsletter.models import Client, MailDeliverySettings


class IndexView(TemplateView):
    template_name = 'newsletter/index.html'
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        count = Client.objects.count()
        context_data['count'] = count
        return context_data


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'comment',)
    success_url = reverse_lazy('newsletter:clients')


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'comment',)

    def get_success_url(self):
        return reverse('newsletter:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('newsletter:clients')


class MailDeliverySettingsCreateView(CreateView):
    model = MailDeliverySettings
    fields = ('name', 'time_start', 'time_stop', 'periodicity', 'subject', 'message')
    success_url = reverse_lazy('newsletter:delivery_view')

    # def form_valid(self, form):
    #     obj = form.save()
    #     make_newsletter()
    #     return super().form_valid(form)


class MailDeliverySettingsListView(ListView):
    model = MailDeliverySettings


class MailDeliverySettingsDetailView(DetailView):
    model = MailDeliverySettings


class MailDeliverySettingsUpdateView(UpdateView):
    model = MailDeliverySettings
    fields = ('name', 'time_start', 'time_stop', 'periodicity', 'subject', 'message')
    success_url = reverse_lazy('newsletter:delivery_detail')

    def get_success_url(self):
        return reverse('newsletter:delivery_detail', args=[self.kwargs.get('pk')])


class MailDeliverySettingsDeleteView(DeleteView):
    model = MailDeliverySettings
    success_url = reverse_lazy('newsletter:delivery_view')
