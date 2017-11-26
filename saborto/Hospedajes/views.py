from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from Hospedajes.models import *
import datetime
from datetime import timedelta
import random

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'show_all_rooms.html')

def search_rooms_view(request):
    if request.method == 'GET':
        return render(request, 'search_rooms.html')

def show_all_rooms_view(request):
    if request.method == 'GET':
        try:
            property = Property.objects.all()

        except:
            property = []
        return render(request, 'show_all_rooms.html', {'rooms': property})

def show_rooms_view(request):
    if request.method == 'GET':
        try:
            city = City.objects.get(name = request.GET['city'])
            pax = request.GET['pax']
            date = request.GET['date']
            property = Property.objects.filter(city = city, maxGuest__gte = pax)

            definitiveProp = []


            for i in property:
                try:
                    property2 =  DateRental.objects.get(property = i,date = date)
                    definitiveProp.append(property2)
                except:
                    pass

        except:
            definitiveProp = []
        return render(request, 'show_rooms.html', {'rooms': definitiveProp})

def show_singleR_view(request,room_id):

    if request.method == 'GET':
        try:
            singular_room = DateRental.objects.get(id=room_id)
            return render_to_response('show_single_room.html', {'room': singular_room})
        except:
            return render_to_response('index.html')

    elif request.method == 'POST':
        try:

            property = Property.objects.get(id=request.POST['propertyId'])

            if dateAble(request.POST['fromD'],request.POST['toD'],property):
                guest = Guest(name=request.POST['name'],surename = request.POST['surname'], email = request.POST['email'])
                guest.save()
                code = random.randint(0, 850000000000000)

                reservation = Reservation(code = code,total = 0, property = property, guest = guest)

                reservation.save()

                saveRangeDate(datetime.datetime.strptime(request.POST['fromD'], "%Y-%m-%d").date(), datetime.datetime.strptime(request.POST['toD'], "%Y-%m-%d").date(), reservation, property)

                countDays = amount(datetime.datetime.strptime(request.POST['fromD'], "%Y-%m-%d").date(),datetime.datetime.strptime(request.POST['toD'], "%Y-%m-%d").date())

                reservation.total = (reservation.property.priceDays * countDays) * 1.08
                reservation.save()

                reservation2 = Reservation.objects.get(property = property, guest = guest,code = code)

                #return render_to_response('index.html')
                return redirect('details', id=reservation.id)


        except:
            print ('Error en la reserva')
    else:
        return render('index.html')

def aaa(request,id):
    if request.method == 'GET':
        r = Reservation.objects.get(id = id )

        return render(request,'details.html',{'r':r})

def dateAble(fromD,toD,property):
    able = True
    try:
        auxDate = DateRental.objects.filter(date__range=[fromD, toD],property = property)
        for a in auxDate:
            if a.reservation is not None:
                able = False
                break

        return able

    except:
        able = False
        return able

def saveRangeDate(fromD, toD, reservation, property):
    while(fromD <= toD):
        dateRent = DateRental.objects.get(date=fromD,property = property)
        dateRent.reservation = reservation
        dateRent.save()
        fromD = fromD + timedelta(days=1)

def amount(fromD,toD):
    countD = 0
    while(fromD <= toD):
        countD = countD +1
        fromD = fromD + timedelta(days=1)
        print (countD)
    return countD