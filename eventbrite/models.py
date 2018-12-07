from django.db import models
import django_filters
from rest_framework import serializers

# Create your models here.


class Event(models.Model):

    name = models.CharField(max_length=1000, blank=True, null=True)
    start = models.DateTimeField(db_index=True, blank=True, null=True)
    min_ticket_cost = models.IntegerField(db_index=True, default=0)
    external_id = models.BigIntegerField()
    organizer_name = models.CharField(max_length=1000, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True, default=None)
    raw_data = models.TextField()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('raw_data', )


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'min_ticket_cost': ['exact', 'lte', 'gte'],
            'start': ['exact', 'gte', 'lte'],
        }

