from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=50, null = False, blank = False)

    def __str__(self):
        return self.name;

class Estate (models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    confort = models.TextField(null=True, blank=True)
    services = models.TextField(null=True, blank=True)
    maxPax = models.IntegerField(null=False, blank=False, default=1)
    price = models.FloatField(null=False, blank=True, default=0)
    image = models.CharField(max_length=200,  null=True, blank=True)
    city = models.ForeignKey(City, null=False, blank=False)
    host = models.OneToOneField(User, null=False, blank=False)

    def __str__(self):
        return self.title;

class Resident(models.Model):
    name = models.CharField(max_length=50, null= False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)

class Booking(models.Model):
    number = models.AutoField(primary_key=True)
    date = models.DateTimeField(null=False, blank=False)
    total_price = models.FloatField(null=False, blank=False)
    resident = models.ForeignKey(Resident, null=False, blank=False)

    def __str__(self):
        return str(self.number) + ". Booking: " + str(self.date.date());

class RentalDate(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    booking = models.ForeignKey(Booking, null=True, blank=True)
    estate = models.ManyToManyField(Estate, null=False, blank=False)

