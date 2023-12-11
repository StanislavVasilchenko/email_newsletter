from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import IndexView, ClientListView, ClientCreateView, ClientDetailView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
]
