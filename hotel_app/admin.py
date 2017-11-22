from django.contrib import admin

# Register your models here.
from hotel_app.models import *

admin.site.register(City)
admin.site.register(Estate)
admin.site.register(Booking)
admin.site.register(Resident)
admin.site.register(RentalDate)

