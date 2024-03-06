from rest_framework import serializers
from event.models import Event
from django.utils import timezone
from event.models import Donation, Event

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'image', 'description', 'created_date', 'event_date']
        read_only_fields = ['created_date']

    def validate_event_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value

  
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
