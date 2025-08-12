from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    party_size = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"