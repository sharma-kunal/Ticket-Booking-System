from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from .serializers import TicketSerializer
import re


# function to Validate Date
def validate_date(date):
    isValid = re.search('([12]\d{3}[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01]))', date)
    if isValid:
        return True
    return False


# function to Validate Time
def validate_time(time):
    isValid = re.search('(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]', time)
    if isValid:
        return True
    return False


# Function to check if limit exceeded for booking ticket for specified Date and Time
def isBookingLimitReached(date, time):
    noOfTickets = 0
    data = Ticket.objects.all()
    for item in data:
        if str(item.date) == date and str(item.time) == time:
            noOfTickets += 1
    return noOfTickets > 20


# Function to check if a Ticket Exists with Ticket ID
def ticketExists(id):
    try:
        data = Ticket.objects.get(id=id)
        return data
    except ObjectDoesNotExist:
        return []


# API URL api/ticket_details
class TicketDetails(APIView):
    def get(self, request):
        date = self.request.query_params.get('date', None)
        time = self.request.query_params.get('time', None)
        msg = ""
        data = Ticket.objects.all()
        result = []

        if date and time:
            # GET ALL TICKETS FOR SPECIFIED DATE AND TIME
            date = date.replace('/', '-')
            isDate = validate_date(date)
            isTime = validate_time(time)
            time += ":00"
            if isDate and isTime:
                for d in data:
                    if str(d.date) == date and str(d.time) == time:
                        result.append(d)
            else:
                if not isDate and not isTime:
                    msg = "Date and Time are in wrong format. Date Format -> YYYY-MM-DD, Time Format -> HH:MM"
                elif not isDate:
                    msg = "Date is in wrong format. Date -> YYYY-MM-DD"
                elif not isTime:
                    msg = "Time is in wrong format. Time -> HH:MM"
        elif date:
            # GET ALL TICKETS FOR SPECIFIED DATE
            isDate = validate_date(date)
            date = date.replace('/', '-')
            if isDate:
                for d in data:
                    if str(d.date) == date:
                        result.append(d)
            else:
                msg = "Date is in wrong format. Date -> YYYY-MM-DD"
        elif time:
            # GET ALL TICKETS FOR SPECIFIED TIME
            isTime = validate_time(time)
            time += ":00"
            if isTime:
                for d in data:
                    if str(d.time) == time:
                        result.append(d)
            else:
                msg = "Time is in wrong format. Time -> HH:MM"
        else:
            # GET ALL TICKETS
            result = data

        if msg:
            return Response({'error': msg}, status=status.HTTP_400_BAD_REQUEST)
        if result:
            serializer = TicketSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No Data found for the specified query'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            date = request.data.get('date')
            time = request.data.get('time')
            if isBookingLimitReached(date, time):
                return Response({'error': f"All tickets for the slot {date} {time} are booked. Please try booking ticket for another slot"},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API URL api/ticket_details/<ticket_id>
class TicketList(APIView):
    def get(self, request, ticket_id):
        data = ticketExists(ticket_id)
        if data:
            serializer = TicketSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': f"Ticket with ID {ticket_id} Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, ticket_id):
        data = ticketExists(ticket_id)
        if data:
            serializer = TicketSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        return Response({'error': f"Ticket with ID {ticket_id} Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, ticket_id):
        data = ticketExists(ticket_id)
        if data:
            data.delete()
            return Response({'status': f"Ticket with Ticket ID {ticket_id} is DELETED"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': f"Ticket with Ticket ID {ticket_id} Not Found"}, status=status.HTTP_404_NOT_FOUND)




