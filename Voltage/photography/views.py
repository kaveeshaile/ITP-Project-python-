from django.shortcuts import render, redirect
from photography.models import photo_test
from django.contrib import messages
from django.http import HttpResponse
from admin_panel.models import reservations
import base64
import admin_panel.views

from django.template import RequestContext
from datetime import date
from datetime import datetime
from admin_panel.models import events
from admin_panel.models import eventbin
from django.utils import timezone
from django.db.models import Q
import calendar
from django.shortcuts import render
from admin_panel.models import events, reservations
from admin_panel.models import eventbin
from admin_panel.models import customer
from admin_panel.models import admin_login
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date
from datetime import datetime
import datetime
from django.utils import timezone
import pymysql


from django.shortcuts import render
#
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse


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


def displaycustomer(request):
    if request.method == 'POST':
        if request.POST.get('checkdate'):

            date = request.POST.get('checkdate')
            booked = reservations.objects.filter(
                Q(S_Time__date=date) | Q(E_Time__date=date))
            print('printing check result:')
            print(booked)
            bookedID = [item.Resources_ID for item in booked]
            photo = photo_test.objects.exclude(PID__in=bookedID)
            return render(request, 'customer_main.html', {'photo_test': photo})

        else:
            messages.warning(request, 'Please Enter the Date!')
            return redirect(request.META.get('HTTP_REFERER'))
    else:

        photo = photo_test.objects.all()
        return render(request, 'customer_main.html', {'photo_test': photo})


def photoprofile(request, id):
    photo = photo_test.objects.filter(id=id)
    return render(request, 'photo_profile.html', {'photo_test': photo})


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


def showreport(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        print("fromdate :" + str(fromdate))
        todate = request.POST.get('todate')
        print("todate :" + str(todate))

        searchresult = reservations.objects.filter(
            Resources_Name="Photography")

        print(searchresult)

        filteredReserves = []

        for i in searchresult:
            sDay = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
            eDay = datetime.datetime.strptime(todate, '%Y-%m-%d')

            if i.S_Time >= sDay and i.E_Time <= eDay:
                filteredReserves.append(i)

        context = {'reservations': filteredReserves}

        template = get_template("photo_report.html")
        report = template.render(context)
        res = BytesIO()

        pdf = pisa.pisaDocument(BytesIO(report.encode("UTF-8")), res)

        if not pdf.err:
            return HttpResponse(res.getvalue(), content_type="application/pdf")
        else:
            return HttpResponse("Error In Generating pdf")

        return render(request, "photo_report.html", context)
    else:
        display = reservations.objects.filter(Resources_Name='Photography')
    return render(request, 'photo_report.html', {'reservations': display})
