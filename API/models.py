from django.db import models

# Create your models here.


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    expired = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.id)
