from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages
from videography.models import video_add
from admin_panel.models import reservations
from videography.models import resources
from datetime import date
import datetime
from django.db.models import Q
from django.shortcuts import redirect
# Create your views here.


def addvideo(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Contact') and request.POST.get('ContactEmail') and request.POST.get('fee'):
         admin = request.session['name']
         saverecord=video_add()
         saverecord.Name = request.POST.get('Name')
         saverecord.Contact = request.POST.get('Contact')
         saverecord.ContactEmail  = request.POST.get('ContactEmail')
         saverecord.Fee = request.POST.get('fee')
         saverecord.Description = request.POST.get('description')
         saverecord.save()
         last = resources.objects.last()
         last.Status = request.POST.get('status')
         last.Admin_ID = admin
         last.save()

        return redirect(displayAlltoAdmin)
    else:
         return render(request,'video_add.html')
     
     
     
     
def displayall(request):
    if request.method == 'POST':
       if request.POST.get('checkdate'):
        date = request.POST.get('checkdate')
        booked = reservations.objects.filter(Q(S_Time__date = date)| Q(E_Time__date = date))
        bookedID = [item.Resources_ID for item in booked]
        videogrpher = video_add.objects.exclude(id__in = bookedID)
        return render(request,'video_customer_main.html',{'videography':videogrpher})
       else:
        messages.warning(request, 'Please Enter the Date!')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        videogrpher = video_add.objects.all()
        return render(request,'video_customer_main.html',{'videography':videogrpher})
    
    
          
def VideographerProfile(request,id):
   
       videogrpher = video_add.objects.filter(id = id)
       return render(request,'video_profile.html',{'videography':videogrpher})
   
   
   
     
def displayAlltoAdmin(request):
      
    if request.method == 'POST':
       if request.POST.get('id'):
        id = request.POST.get('id')
        videogrpher = video_add.objects.filter(id = id)
       return render(request,'video_update.html',{'videography':videogrpher})
    else:
      
        videogrpher = video_add.objects.all()
        return render(request,'video_recently_added.html',{'videography':videogrpher})
        
        

      
def RemoveVideoGrapher(request,id):
   
       videogrpher = video_add.objects.filter(id = id)
       resource = resources.objects.filter(Resources_ID = id)
       videogrpher.delete()
       resource.delete()
       return redirect(displayAlltoAdmin) 
   
   
#def DisplayUpdate(request,id):
       
      #videogrpher = video_add.objects.filter(id = id)
      #return render(request,'video_edit.html',{'videography':videogrpher})
    
   
def UpdateVideoGrapher(request):
    if request.method == 'POST':
       if request.POST.get('Name'):
        id =  request.POST.get('id')
        vid = video_add.objects.get(id = id)
        vid.Name =  request.POST.get('Name')
        vid.Fee =  request.POST.get('fee')
        vid.Contact =  request.POST.get('Contact')
        vid.ContactEmail =  request.POST.get('ContactEmail')
        vid.Description =  request.POST.get('description')
        vid.save()
       return redirect(displayAlltoAdmin) 
    else:
           
           
         return render(request,'video_add.html')
   
    
def bookVideographer(request):
 if request.method == 'POST':
      if request.POST.get('bookingdate'):
    
         date = request.POST.get('bookingdate')
         videographer=reservations()
         videographer.S_Time = request.POST.get('bookingdate')
         videographer.E_Time = request.POST.get('enddate')
         videographer.Event_ID = '2'
         vid = request.POST.get('vid')
         videographer.Resources_ID = vid
         mydate = date[0:10];
         converted_date = datetime.datetime.strptime(mydate, "%Y-%m-%d").date()
         
         if converted_date < datetime.datetime.now().date():
            messages.warning(request, 'Please Enter a valid Date')
            return redirect(request.META.get('HTTP_REFERER')) 
         else: 
             
            if reservations.objects.filter(S_Time__date  = converted_date, Resources_ID = vid ):
                   
                 messages.warning(request, 'Please check availability before make a reservation')
                 return redirect(request.META.get('HTTP_REFERER')) 
            
            else:
                videographer.save()
                return redirect(displayall)
        
            
      else:
         messages.warning(request, 'Please Fill the required Fields!')
         return redirect(request.META.get('HTTP_REFERER'))
 else:
    return redirect(displayall)
       
