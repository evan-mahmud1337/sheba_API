from django.contrib import admin
from .models import Donation, Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'created_date']
    list_filter = ['title', 'event_date']
    search_fields = ['title']


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'amount', 'note']
    list_filter = ['full_name']
    search_fields = ['full_name']