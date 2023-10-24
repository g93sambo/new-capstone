from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateTimeField()

    

class Menu(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(max_length=5)

  