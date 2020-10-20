from django.shortcuts import render, redirect
from photography.models import photo_test
from django.contrib import messages
from django.http import HttpResponse
from admin_panel.models import reservations
import base64
from django.template import RequestContext
from datetime import date
import datetime
from admin_panel.models import events
from admin_panel.models import eventbin

from django.db.models import Q

# Create your views here.


def addPhoto(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('exp') and request.POST.get('des'):
            saverecord = photo_test()
            saverecord.name = request.POST.get('name')
            saverecord.exp = request.POST.get('exp')
            saverecord.des = request.POST.get('des')
            saverecord.phone = request.POST.get('phone')
            saverecord.email = request.POST.get('email')
            saverecord.FB = request.POST.get('FB')
            saverecord.fee = request.POST.get('fee')

            saverecord.profile_image = 'images/pic.jpg'
            saverecord.sample_image1 = 'images/1.jpg'
            saverecord.sample_image2 = 'images/2.jpg'
            saverecord.sample_image3 = 'images/3.jpg'
            saverecord.sample_image4 = 'images/4.jpg'

            saverecord.save()
            messages.success(request, 'Data saved Successfuly..!')
            # return render(request, 'photo_add.html')
            return render(request, 'photo_admin_display.html', {'photo_test': photo_test.objects.all()})
        else:
            return render(request, 'photo_add.html')

    else:
        return render(request, 'photo_add.html')

 # DISPLAY customer main page


# show details one by one..
def displayone(request):
    if request.method == 'POST':
        if request.POST.get('pid'):
            id = request.POST.get('pid')

            return render(request, 'photo_profile.html', {'photo_test': photo_test.objects.filter(id=id)})
        else:
            return render(request, 'photo_admin_display.html', {'photo_test': photo_test.objects.all()})
    else:
        return render(request, 'photo_admin_display.html', {'photo_test': photo_test.objects.all()})


# delete admin side

def admindelete(request, id):

    photographer = photo_test.objects.filter(id=id)
    photographer.delete()
    return render(request, 'photo_admin_display.html', {'photo_test': photo_test.objects.all()})

   # photo = photo_test.objects.get(id=id)

    # if request.method == "POST":
    # photo_test.delete()
    # return redirect("photo_admin_display.html")
    # return render(request, "photo_admin_display.html", context)


def GetDetailsForUpdate(request, id):

    photo = photo_test.objects.get(id=id)
    return render(request, 'photo_update.html', {'photo': photo})


def AdminUpdate(request, id):
    if request.method == 'POST':
       # if request.POST.get('PID') and request.POST.get('name') and request.POST.get('exp') and request.POST.get('des'):
        # saverecord = photo_test()
        # id = request.POST.get('id')
        photo = photo_test.objects.get(id=id)
        photo.PID = request.POST.get('PID')
        photo.name = request.POST.get('name')
        photo.exp = request.POST.get('exp')
        photo.des = request.POST.get('des')
        photo.phone = request.POST.get('phone')
        photo.email = request.POST.get('email')
        photo.FB = request.POST.get('FB')
        photo.fee = request.POST.get('fee')
        photo.save()

        return redirect(displayone)

    else:
        return render(request, 'photo_add.html')


<<<<<<< HEAD
# def displayall(request):
#     if request.method == 'POST':
#         if request.POST.get('checkdate'):
=======
def displaycustomer(request):
    if request.method == 'POST':
        if request.POST.get('checkdate'):
>>>>>>> 729c4437678e5ba9bc486796cb797c67421f7825

#             date = request.POST.get('checkdate')
#             booked = reservations.objects.filter(
#                 Q(S_Time__date=date) | Q(E_Time__date=date))
#             print('printing check result:')
#             print(booked)
#             bookedID = [item.Resources_ID for item in booked]
#             photo = photo_test.objects.exclude(PID__in=bookedID)
#             return render(request, 'customer_main.html', {'photo_test': photo})

#         else:
#             messages.warning(request, 'Please Enter the Date!')
#             return redirect(request.META.get('HTTP_REFERER'))
#     else:

#         photo = photo_test.objects.all()
#         return render(request, 'customer_main.html', {'photo_test': photo})


def photoprofile(request, id):
    photo = photo_test.objects.filter(id=id)
    return render(request, 'photo_profile.html', {'photo_test': photo})


<<<<<<< HEAD
# def bookphotographer(request):
#     if request.method == 'POST':
#         if request.POST.get('bookingdate') and request.POST.get('enddate'):

#             EventID = request.session['E001']
#             date = request.POST.get('bookingdate')
#             photographer = reservations()
#             photographer.S_Time = request.POST.get('bookingdate')
#             photographer.E_Time = request.POST.get('enddate')
#             photographer.Event_ID = EventID
#             PID = request.POST.get('PID')
#             photographer.Resources_ID = PID
#             mydate = date[0:10]
#             converted_date = datetime.datetime.strptime(
#                 mydate, "%Y-%m-%d").date()

#             if converted_date < datetime.datetime.now().date():
#                 messages.warning(request, 'Please Enter a valid Date')
#                 return redirect(request.META.get('HTTP_REFERER'))
#             else:

#                 if reservations.objects.filter(S_Time__date=converted_date, Resources_ID=PID):

#                     messages.warning(
#                         request, 'Please check availability before make a reservation')
#                     return redirect(request.META.get('HTTP_REFERER'))

#                 else:
#                     photographer.save()
#                     return render(request, 'main_reservation_page.html')

#         else:
#             messages.warning(request, 'Please Fill the required Fields!')
#             return redirect(request.META.get('HTTP_REFERER'))
#     else:
#         return redirect(displayall)
=======
def bookphotographer(request):
    if request.method == 'POST':
        if request.POST.get('bookingdate') and request.POST.get('enddate'):

            EventID = request.session['eventID']
            date = request.POST.get('bookingdate')
            photographer = reservations()
            photographer.S_Time = request.POST.get('bookingdate')
            photographer.E_Time = request.POST.get('enddate')
            photographer.Event_ID = EventID
            PID = request.POST.get('PID')
            photographer.Resources_ID = PID
            photographer.Resources_Name = 'Photography'

            mydate = date[0:10]
            converted_date = datetime.datetime.strptime(
                mydate, "%Y-%m-%d").date()

            if converted_date < datetime.datetime.now().date():
                messages.warning(request, 'Please Enter a valid Date')
                return redirect(request.META.get('HTTP_REFERER'))
            else:

                if reservations.objects.filter(S_Time__date=converted_date, Resources_ID=PID):

                    messages.warning(
                        request, 'Please check availability before make a reservation')
                    return redirect(request.META.get('HTTP_REFERER'))

                else:
                    photographer.save()
                    return render(request, 'main_reservation_page.html')

        else:
            messages.warning(request, 'Please Fill the required Fields!')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(displaycustomer)


def getmonthlyreportforphotographer(request):
    if request.method == 'POST':
        getmonth = request.POST.get('month')
        converted_date = datetime.datetime.strptime(getmonth, "%Y-%m").date()
        year = converted_date.year
        month = converted_date.month

        eve = events.objects.filter(Date__year=year).filter(Date__month=month)
        ended = eventbin.objects.filter(
            Date__year=year).filter(Date__month=month)
        context = {'event': eve, 'completed_events': ended,
                   'getmonth': getmonth}

        return render(request, 'main_report.html', context=context)

    return render(request, 'main_report.html')
>>>>>>> 729c4437678e5ba9bc486796cb797c67421f7825
