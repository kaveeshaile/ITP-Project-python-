from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from soundsystems.models import sound_admin_upload
from django.shortcuts import redirect




def sound_insert(request): 
    
        if request.method == 'POST': 		
             if request.POST.get('packname') and request.POST.get('suitable') and request.POST.get('brand') and request.POST.get('price'):
                mydata=sound_admin_upload()
                mydata.Package_name = request.POST.get('packname')
                mydata.Suitable_for = request.POST.get('suitable')
                mydata.Brand = request.POST.get('brand')
                mydata.Price = request.POST.get('price')
               
                mydata.save()

             return redirect(sound_update)
                    
        else:
            return render(request,'sound_admin_upload.html')
    
    


def sound_update(request): 
   if request.method == 'POST':
        if request.POST.get('packname'):
         id =  request.POST.get('id')
         sound = sound_admin_upload.objects.get(id = id)
         sound.Package_name =  request.POST.get('packname')
         sound.Suitable_for =  request.POST.get('suitable')
         sound.Price =  request.POST.get('price')   
         sound.save()
    
        return redirect(sound_userview) 
   else:
      
        return render(request,'sound_update.html')
     
    



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





     
     
   
       


def sound_main(request): 
        return render(request, 'sound_main.html')





