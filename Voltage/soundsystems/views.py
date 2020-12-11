from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from soundsystems.models import sound_admin
from django.shortcuts import redirect
import datetime
from admin_panel.models import reservations
from admin_panel.models import events




def sound_insert(request): 
    
        if request.method == 'POST': 		
             if request.POST.get('packname') and request.POST.get('suitable') and request.POST.get('brand') and request.POST.get('price'):
                mydata=sound_admin()
                mydata.Package_name = request.POST.get('packname')
                mydata.Suitable_for = request.POST.get('suitable')
                mydata.Brand = request.POST.get('brand')
                mydata.Price = request.POST.get('price')
                #mydata.packageImg = request.FILES.get('packageImg')
               
                mydata.save()
                messages.success(request, 'Package Data Saved Successfully')

                return redirect(display_customers)
                    
        else:
            #return render(request,'sound_admin_upload.html')
            return render(request,'sound_admin_upload.html')
    
    


def sound_admin_update(request):

   if request.method == "POST":
        if request.POST.get('id'):
         id =  request.POST.get('id')
         sound = sound_admin.objects.get(id = id)
         #print(sound)
         sound.Package_name =  request.POST.get('packname')
         sound.Suitable_for =  request.POST.get('suitable')
         sound.Brand =  request.POST.get('brand')
         sound.Price =  request.POST.get('price')
         sound.save()
         return render(request,'sound_admin_upload.html')
        
        
   else:
      
         return render(request,'sound_admin_upload.html')
     






def sound_display_admin(request):
   
     sound = sound_admin.objects.all();
     #context = {'sound_admin': sound}
     #return render(request,'sound_test.html',{'soundsystem':sound})
     #return render(request,'sound_test.html', context=context)
     return render(request,'sound_update.html',{'soundsystem':sound})



def edit(request,id):

    #if request.method == "POST":
     #id =  request.POST.get('id')
     sound = sound_admin.objects.filter(id=id)
     #context = {'sound_admin': sound}
     #return render(request, 'sound_test2.html', context=context)
     #return render(request,'sound_test2.html',{'soundadmin':sound})
     
     return render(request,"sound_admin_control.html",{"soundsystem":sound})

    


def display_customers(request):
    
     sound = sound_admin.objects.all();
     #context = {'sound_admin': sound_admin}

     return render(request,'sound_userview.html',{'soundsystem':sound})



def sound_delete(request, id):
    sound = sound_admin.objects.filter(id=id)
    sound.delete()
    return render(request,'sound_admin_upload.html')




def bookSoundPackages(request):
 if request.method == 'POST':
     if request.POST.get('bookingdate') and request.POST.get('enddate'):
          
           eventID = request.session['eventID']
           date = request.POST.get('bookingdate')
           soundbook = reservations()
           soundbook.S_Time = request.POST.get('bookingdate')
           soundbook.E_Time = request.POST.get('enddate')
           soundbook.Event_ID = eventID
           soundbook.Resources_Name = 'Soundsystem'
           sound = request.POST.get('id')
           soundbook.Resources_ID = sound
           mydate = date[0:10];
           converted_date = datetime.datetime.strptime(mydate, "%Y-%m-%d").date()
         
           if converted_date < datetime.datetime.now().date():
            messages.warning(request, 'Please Enter a valid Date')
            return redirect(request.META.get('HTTP_REFERER')) 
           else: 
             
               if reservations.objects.filter(S_Time__date  = converted_date, Resources_ID = sound ):
                   
                 messages.warning(request, 'Please check availability before make a reservation')
                 return redirect(request.META.get('HTTP_REFERER')) 
            
               else:
                 soundbook.save()
                 return render(request, 'main_reservation_page.html')
        
            
     else:
                messages.warning(request, 'Please Fill the required Fields!')
                return redirect(request.META.get('HTTP_REFERER'))
 else:
      return redirect(display_customers)


 





