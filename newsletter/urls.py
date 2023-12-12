from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import (IndexView, ClientListView, ClientCreateView,
                              ClientDetailView, ClientUpdateView, ClientDeleteView, MailDeliverySettingsCreateView)

app_name = NewsletterConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('delivery_create/', MailDeliverySettingsCreateView.as_view(), name='delivery_create'),
]
