from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from soundsystems.models import sound_admin_upload
from django.shortcuts import redirect




def sound_insert(request): 
    
        if request.method == 'POST': 		
             if request.POST.get('packname') and request.POST.get('suitable') and request.POST.get('price'):
                saverecord=sound_admin_upload()
                saverecord.Package_name = request.POST.get('packname')
                saverecord.Suitable_for = request.POST.get('suitable')
                saverecord.Price = request.POST.get('price')
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
                        sound = sound_admin_upload.objects.filter(id = id)
                        return render(request, 'sound_reservation.html',{'soundsystems':sound})
        
        else:

                sound = sound_admin_upload.objects.all()
                return render(request, 'sound_userview.html',{'soundsystems':sound})




def sound_update(request): 


        sound = sound_admin_upload.objects.all()

        return render(request, 'sound_update.html',{'soundsystems':sound})


def sound_main(request): 
        return render(request, 'sound_main.html')





