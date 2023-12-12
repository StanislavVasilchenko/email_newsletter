from django.contrib import admin

from newsletter.models import Client, MailDeliverySettings


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment',)


@admin.register(MailDeliverySettings)
class MailDeliverySettingsAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_stop', 'periodicity', 'status', 'subject', 'message')
    list_filter = ('status',)
