import json
from datetime import timedelta
from dateutil import parser
from django.test import Client
from django.test import TestCase
from django.urls import reverse
import factory

from eventbrite.models import Event


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    id = factory.Sequence(lambda n: n)
    external_id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Event name #{}'.format(n))
    organizer_name = factory.Sequence(lambda n: 'Organizer name #{}'.format(n))
    min_ticket_cost = factory.Sequence(lambda n: 10 * n)
    start = factory.Sequence(lambda n: parser.parse('2018-12-08T03:00:00Z') + timedelta(days=n))
    currency = 'USD'


class EventListTestCase(TestCase):
    def setUp(self):
        self.events = EventFactory.create_batch(11)
        self.client = Client()

    def test_list_events(self):
        response = self.client.get(reverse('eventbrite:event-list'))
        data = response.json()

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data['results']), 10)
        self.assertIsNotNone(data['next'])

        response = self.client.get(data['next'])
        data = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data['results']), 1)


class EventRetrieveTestCase(TestCase):
    def setUp(self):
        self.events = EventFactory.create_batch(2)
        self.client = Client()

    def test_retrieve_event(self):
        response = self.client.get(reverse('eventbrite:event-detail', args=(1,)))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.json(),
            {
                'id': 1,
                'external_id': 1,
                'name': 'Event name #1',
                'organizer_name': 'Organizer name #1',
                'min_ticket_cost': 10,
                'start': '2018-12-09T03:00:00Z',
                'currency': 'USD',
            }

        )


class EventUpdateTestCase(TestCase):
    def setUp(self):
        self.events = EventFactory()
        self.client = Client()

    def test_retrieve_event(self):
        response = self.client.patch(reverse('eventbrite:event-detail', args=(0,)), data=json.dumps(
            {
                'external_id': 99,
                'name': 'New name',
                'organizer_name': 'New organizer name',
                'min_ticket_cost': 199,
            }
        ), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('eventbrite:event-detail', args=(0,)))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.json(),
            {
                'id': 0,
                'external_id': 99,
                'name': 'New name',
                'organizer_name': 'New organizer name',
                'min_ticket_cost': 199,
                'start': '2018-12-08T03:00:00Z',
                'currency': 'USD',
            }
        )



