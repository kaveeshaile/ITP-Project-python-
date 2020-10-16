from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from soundsystems.models import sound_admin_upload
from django.shortcuts import redirect



def sound_admin_upload(request): 
    
     if request.method == 'POST':
             if request.POST.get('Packn') and request.POST.get('Suitable') and request.POST.get('Brand') and request.POST.get('Price'):
                    saverecord=sound_admin_upload()
                    saverecord.Package_name = request.POST.get('Packn')
                    saverecord.Suitable_for = request.POST.get('Suitable')
                    saverecord.Brand  = request.POST.get('Brand')
                    saverecord.Price = request.POST.get('Price')
                    saverecord.Description = request.POST.get('sounddescription')
                    saverecord.save()
                    return redirect(sound_update)
     else:
                    return render(request,'sound_admin_upload.html')
    
    

    


def sound_reservation(request): 
        
        
        
        
        
        return render(request, 'sound_reservation.html')


 
def sound_userview(request): 
        
        if request.method == "POST":
                if request.POST.get('id'):
                        id = request.POST.get('id')
                        sound = sound_admin.objects.filter(id = id)
                        return render(request, 'sound_reservation.html',{'soundsystems':sound})
        
        else:

                sound = sound_admin.objects.all()
                return render(request, 'sound_userview.html',{'soundsystems':sound})




def sound_update(request): 


        sound = sound_admin.objects.all()

        return render(request, 'sound_update.html',{'soundsystems':sound})


def sound_main(request): 
        return render(request, 'sound_main.html')





