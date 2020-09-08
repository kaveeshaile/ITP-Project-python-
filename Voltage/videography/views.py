from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from videography.models import video_add
from django.shortcuts import redirect
# Create your views here.


def addvideo(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Contact') and request.POST.get('ContactEmail') and request.POST.get('fee'):
         saverecord=video_add()
         saverecord.Name = request.POST.get('Name')
         saverecord.Contact = request.POST.get('Contact')
         saverecord.ContactEmail  = request.POST.get('ContactEmail')
         saverecord.Fee = request.POST.get('fee')
         saverecord.Description = request.POST.get('description')
         saverecord.save()
        return redirect(displayall)
    else:
         return render(request,'video_add.html')
     
def displayall(request):
        videogrpher = video_add.objects.all()
        return render(request,'display_all_vid.html',{'videography':videogrpher})
     
     
def displaytocustomer(request):
         return render(request,'cus_vid_profile.html')
