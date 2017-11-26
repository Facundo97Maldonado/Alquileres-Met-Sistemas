from django.contrib import admin
from Hospedajes.models import *

class AdminCity(admin.ModelAdmin):
    search_fields = ['name']

class DateRental_Inline(admin.TabularInline):
    model = DateRental
    fk_name = 'property'
    max_num = 7

class AdminPropery(admin.ModelAdmin):
    search_fields = ['numberCard']
    list_filter = ('numberCard',)
    ordering = ('title',)
    inlines = [DateRental_Inline, ]


# Register your models here.

admin.site.register(City, AdminCity)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Property,AdminPropery,)
