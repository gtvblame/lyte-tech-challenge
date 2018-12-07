import json

from django.core.management.base import BaseCommand, CommandError
from eventbrite.models import Event


class Command(BaseCommand):
    help = 'Loads events from fixtures into the database'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', required=True, type=str)

    def handle(self, *args, **options):
        Event.objects.all().delete()

        fp = open(options['filename'])
        events = json.load(fp)['events']

        event_objects = map(
            lambda event: Event(
                name=event['name']['text'],
                start=event['start']['utc'],
                min_ticket_cost=min(
                    self._extract_min_ticket_cost(ticket)
                    for ticket in event['ticket_classes']
                ),
                external_id=int(event['id']),
                organizer_name=event['organizer']['name'],
                currency=event['currency'],
                raw_data=event,
            ),
            events
        )

        Event.objects.bulk_create(event_objects)

    def _extract_min_ticket_cost(self, ticket):
        if ticket['free'] is True or ticket['donation'] is True:
            return 0
        else:
            return ticket['cost']['value'] + ticket['fee']['value'] + ticket['tax']['value']

