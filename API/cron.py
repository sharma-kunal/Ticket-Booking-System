from .models import Ticket
from datetime import datetime


def markTicketsExpired():
    tickets = Ticket.objects.filter(expired=False)
    current_time = datetime.now()
    for ticket in tickets:
        ticket_time = datetime.combine(ticket.date, ticket.time)
        diff = current_time-ticket_time

        # Difference is of greater than 1 day (Mark as Expired)
        if diff.days > 0:
            # mark ticket as expired
            ticket.expired = True
            ticket.save()
        elif diff.days == 0 and diff.seconds/3600 >= 8.0:
            # mark ticket expired
            ticket.expired = True
            ticket.save()


def deleteExpiredTickets():
    tickets = Ticket.objects.filter(expired=True)
    for ticket in tickets:
        ticket.delete()
