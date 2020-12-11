from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib import messages
from videography.models import video_add
from admin_panel.models import reservations
from videography.models import resources
from videography.models import video_samples
from admin_panel.models import events
from datetime import date
import datetime
from django.db.models import Q
from django.shortcuts import redirect
import base64

# Create your views here.


def addvideo(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Contact') and request.POST.get('ContactEmail') and request.POST.get('fee'):
            admin = request.session['name']
            video = video_add()
            video.Name = request.POST.get('Name')
            video.Contact = request.POST.get('Contact')
            video.ContactEmail = request.POST.get('ContactEmail')
            video.Fee = request.POST.get('fee')
            video.Status = request.POST.get('status')
            video.Description = request.POST.get('description')
            video.profile_pic = request.FILES.get('profile_pic')
            video.save()
            last = resources.objects.last()
            last.Status = request.POST.get('status')
            last.Admin_ID = admin
            last.save()
            sample1 = video_samples.objects.last()
            sample1.Samples = request.FILES.get('sample')
            sample1.save()

        return redirect(displayAlltoAdmin)
    else:
        return render(request, 'video_add.html')


def displayall(request):
    if request.method == 'POST':

        if request.POST.get('checkdate'):

            date = request.POST.get('checkdate')
            booked = reservations.objects.filter(
                Q(S_Time__date=date) | Q(E_Time__date=date))
            bookedID = [item.Resources_ID for item in booked]
            videogrpher = video_add.objects.filter(
                Status='In').exclude(id__in=bookedID)
            return render(request, 'video_customer_main.html', {'videography': videogrpher})

        else:

            messages.warning(request, 'Please Enter the Date!')
            return redirect(request.META.get('HTTP_REFERER'))

    else:

        check = resources.objects.filter(Status="Out")
        checkId = [item.Resources_ID for item in check]
        videogrpher = video_add.objects.exclude(id__in=checkId)
        return render(request, 'video_customer_main.html', {'videography': videogrpher})


def VideographerProfile(request, id):

    videographer = video_add.objects.filter(id=id)
    samples = video_samples.objects.filter(Resources_ID=id)
    context = {'videography': videographer, 'video_samples': samples}
    return render(request, 'video_profile.html', context=context)


def displayAlltoAdmin(request):

    videographer = video_add.objects.all()
    return render(request, 'video_recently_added.html', {'videography': videographer})


def displayProfiletoAdmin(request, id):
    videographer = video_add.objects.filter(id=id)
    samples = video_samples.objects.filter(Resources_ID=id)
    res = resources.objects.filter(Resources_ID=id)
    context = {'videography': videographer,
               'video_samples': samples, 'resources': res}
    return render(request, 'video_update.html', context=context)


def RemoveVideoGrapher(request, id):

    videogrpher = video_add.objects.filter(id=id)
    resource = resources.objects.filter(Resources_ID=id)
    sample = video_samples.objects.filter(Resources_ID=id)
    videogrpher.delete()
    resource.delete()
    sample.delete()
    return redirect(displayAlltoAdmin)


# def DisplayUpdate(request,id):

   #videogrpher = video_add.objects.filter(id = id)
   # return render(request,'video_edit.html',{'videography':videogrpher})


def UpdateVideoGrapher(request):
    if request.method == 'POST':
        if request.POST.get('Name'):
            id = request.POST.get('id')
            vid = video_add.objects.get(id=id)
            sam = video_samples.objects.get(Resources_ID=id)
            res = resources.objects.get(Resources_ID=id)
            vid.Name = request.POST.get('Name')
            vid.Fee = request.POST.get('fee')
            vid.Contact = request.POST.get('Contact')
            vid.Status = request.POST.get('status')
            vid.ContactEmail = request.POST.get('ContactEmail')
            vid.Description = request.POST.get('description')
            res.Status = request.POST.get('status')
            profilpic = request.FILES.get('profile_pic')
            res.save()

            if profilpic == None:  # check if profile picture changed
                vid.save()
            else:
                vid.profile_pic = profilpic
                vid.save()

            sam.Samples = request.FILES.get('sample')
            if request.FILES.get('sample') == None:

                print('null')
            else:

                sam.save()

        return redirect(displayAlltoAdmin)
    else:

        return render(request, 'video_add.html')


def bookVideographer(request):
    if request.method == 'POST':
        if request.POST.get('bookingdate') and request.POST.get('enddate'):

            eventID = request.session['eventID']
            date = request.POST.get('bookingdate')
            videographer = reservations()
            videographer.S_Time = request.POST.get('bookingdate')
            videographer.E_Time = request.POST.get('enddate')
            videographer.Event_ID = eventID
            videographer.Resources_Name = 'Videography'
            vid = request.POST.get('vid')
            videographer.Resources_ID = vid
            mydate = date[0:10]
            converted_date = datetime.datetime.strptime(
                mydate, "%Y-%m-%d").date()

            if converted_date < datetime.datetime.now().date():
                messages.warning(request, 'Please Enter a valid Date')
                return redirect(request.META.get('HTTP_REFERER'))
            else:

                if reservations.objects.filter(S_Time__date=converted_date, Resources_ID=vid):

                    messages.warning(
                        request, 'Please check availability before make a reservation')
                    return redirect(request.META.get('HTTP_REFERER'))

                else:
                    videographer.save()
                    return redirect(submitEvent)

        else:
            messages.warning(request, 'Please Fill the required Fields!')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(displayall)


def CreateEvent(request):

    cusID = '88'  # temporary hardcode value should be login session
    if request.method == 'POST':
        if request.POST.get('eventDate'):

            date = request.POST.get('eventDate')
            converted_date = datetime.datetime.strptime(
                date, "%Y-%m-%d").date()

            if converted_date < datetime.datetime.now().date():

                messages.warning(request, 'Please Enter a valid Date')
                return redirect(request.META.get('HTTP_REFERER'))
            else:

                event = events()
                event.Date = request.POST.get('eventDate')
                event.Event_type = request.POST.get('type')
                event.Location = request.POST.get('location')
                event.Contact = request.POST.get('contact')
                event.Customer_ID = cusID
                event.OnCreateTime = datetime.datetime.now()
                event.save()
                last = events.objects.last()
                eID = last.Event_ID
                print(eID)
                request.session['eventID'] = eID
                eve = events.objects.filter(Event_ID=eID)
                return render(request, 'main_reservation_page.html', {'event': eve})
        else:
            messages.warning(request, 'Please enter the event date!')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        if cusID is None:
            # should redirect to registration page
            return render(request, 'home.html')
        else:
            return render(request, 'event_create.html')


def submitEvent(request):
    id = request.session['eventID']

    if request.method == 'POST':

        if reservations.objects.filter(Event_ID=id):
            event = events.objects.get(Event_ID=id)
            event.Status = 'waiting'
            event.Event_type = request.POST.get('type')
            event.Location = request.POST.get('location')
            event.Contact = request.POST.get('contact')
            event.save()
            return render(request, 'home.html')

        else:
            event = events.objects.get(Event_ID=id)
            messages.warning(
                request, 'You can"t submit an empty event! Make at least one Reservation')
            return render(request, 'main_reservation_page.html')

    else:
        eve = events.objects.filter(Event_ID=id)
        res = reservations.objects.filter(Event_ID=id)
        context = {'event': eve, 'reservations': res}
        return render(request, 'main_reservation_page.html', context=context)


def CancelEvent(request, id):
    event = events.objects.filter(Event_ID=id)
    event.delete()
    res = reservations.objects.filter(Event_ID=id)
    if res != None:
        res.delete()
        del request.session['eventID']
        messages.warning(request, 'Event deleted')
        return redirect(CreateEvent)

    else:
        messages.warning(request, 'Somethin went wrong..')
        return redirect(request.META.get('HTTP_REFERER'))
