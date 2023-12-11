from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import IndexView, ClientListView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
]
