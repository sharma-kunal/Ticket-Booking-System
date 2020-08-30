from django.test import TestCase, Client
from .models import Ticket
from django.urls import reverse
from rest_framework import status
from .serializers import TicketSerializer
import json

client = Client()


class GetAllTicketsTest(TestCase):
    """ Test module to GET all tickets API """

    def setUp(self) -> None:
        self.User1 = Ticket.objects.create(name='User1', phone_number='00000000', date='2020-08-29', time='15:30',
                                           expired=False)
        self.User2 = Ticket.objects.create(name='User1', phone_number='00000000', date='2020-08-30', time='13:00',
                                           expired=False)
        self.User3 = Ticket.objects.create(name='User1', phone_number='00000000', date='2020-09-1', time='11:00',
                                           expired=False)

    def test_get_all_tickets(self):
        response = client.get(reverse('get_post_tickets'))
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleTicketTest(TestCase):
    """ Test module to GET single ticket API """

    def setUp(self) -> None:
        self.User1 = Ticket.objects.create(name='User1', phone_number='00000000', date='2020-08-29', time='15:30',
                                           expired=False)
        # self.User2 = Ticket.objects.create(phone_number='00000000', date='2020-08-30', time='15:30',
        #                                    expired=False)
        # self.User3 = Ticket.objects.create(name='User1', date='2020-08-29', time='15:30',
        #                                    expired=False)
        # self.User4 = Ticket.objects.create(name='User1', phone_number='00000000', time='15:30',
        #                                    expired=False)
        # self.User5 = Ticket.objects.create(name='User1', phone_number='00000000', date='2020-08-29', expired=False)

    def test_get_valid_single_ticket(self):
        response = client.get(reverse('get_put_delete_ticket', kwargs={'ticket_id': self.User1.id}))
        ticket = Ticket.objects.get(id=self.User1.id)
        serializer = TicketSerializer(ticket)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_ticket(self):
        response = client.get(reverse('get_put_delete_ticket', kwargs={'ticket_id': 1000000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewTicketTest(TestCase):
    """ Test module for inserting a new ticket """

    def setUp(self) -> None:
        self.validTicket = {
            'name': 'User1',
            'phone_number': '00000000',
            'date': '2020-08-29',
            'time': '15:00',
            'expired': False
        }
        # Name field is missing is missing
        self.invalidTicket1 = {
            'phone_number': '00000000',
            'date': '2020-08-29',
            'time': '15:00',
            'expired': False
        }

        # Phone_number field is missing
        self.invalidTicket2 = {
            'name': 'User1',
            'date': '2020-08-29',
            'time': '15:00',
            'expired': False
        }

        # Date OR Time format is wrong
        self.invalidTicket3 = {
            'name': 'User1',
            'phone_number': '00000000',
            'date': '29-08-2020',
            'time': '15:00',
            'expired': False
        }

    def test_create_valid_ticket(self):
        response = client.post(reverse('get_post_tickets'), data=json.dumps(self.validTicket), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_ticket(self):
        def get_response(data):
            response = client.post(reverse('get_post_tickets'), data=json.dumps(data), content_type='application/json')
            return response.status_code

        self.assertEqual(get_response(self.invalidTicket1), status.HTTP_400_BAD_REQUEST)
        self.assertEqual(get_response(self.invalidTicket2), status.HTTP_400_BAD_REQUEST)
        self.assertEqual(get_response(self.invalidTicket3), status.HTTP_400_BAD_REQUEST)


class UpdateSingleTicketTest(TestCase):
    """ Test module for updating an existing ticket record """

    def setUp(self) -> None:
        self.User1 = Ticket.objects.create(name='User1', phone_number='00000000', date='2020-08-29', time='15:30',
                                           expired=False)
        self.User2 = Ticket.objects.create(name='User2', phone_number='00000000', date='2020-08-30', time='13:30',
                                           expired=False)

        self.valid_payload = {
            'name': 'User1',
            'phone_number': '00000000',
            'date': '2020-08-29',
            'time': '13:00',
            'expired': False
        }

        self.invalid_payload = {
            'name': '',
            'phone_number': '00000000',
            'date': '2020-08-30',
            'time': '13:00',
            'expired': False
        }

    def test_valid_update_ticket(self):
        response = client.put(reverse('get_put_delete_ticket', kwargs={'ticket_id': self.User1.id}),
                              data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_update_ticket(self):
        response = client.put(reverse('get_put_delete_ticket', kwargs={'ticket_id': self.User2.id}),
                              data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)


class DeleteSingleTicketTest(TestCase):
    """ Test module for deleting an existing ticket record """

    def setUp(self) -> None:
        self.User1 = Ticket.objects.create(name='User1', phone_number='00000000', date='2020-08-29', time='15:30',
                                           expired=False)

    def test_valid_delete_ticket(self):
        response = client.delete(reverse('get_put_delete_ticket', kwargs={'ticket_id': self.User1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_ticket(self):
        response = client.delete(reverse('get_put_delete_ticket', kwargs={'ticket_id': 1000000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
