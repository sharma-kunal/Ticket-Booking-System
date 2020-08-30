from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    expired = serializers.BooleanField(required=False)

    class Meta:
        model = Ticket
        fields = '__all__'
