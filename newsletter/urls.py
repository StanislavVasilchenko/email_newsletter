from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import IndexView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
