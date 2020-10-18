from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from soundsystems.models import sound_admin
from django.shortcuts import redirect




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
            return render(request,'sound_admin_upload.html')
    
    


def sound_admin_update(request): 

   #if request.method == 'POST':
       
         #id =  request.POST.get('id')
         sound = sound_admin.objects.all();
         #sound.Package_name =  request.POST.get('packname')
         #sound.Suitable_for =  request.POST.get('suitable')
         #sound.Price =  request.POST.get('price')   
         #sound.save()
    
         #return redirect(dis_inserted_info) 
         context = {'sound_admin': sound_admin}
         #return render(request, 'sound_update.html', context)
         return render(request,'sound_update.html',{'soundadmin':sound})
   #else:
      
        #return render(request,'sound_admin_upload.html')



def display_customers(request):
    
     sound = sound_admin.objects.all();
     context = {'sound_admin': sound_admin}

     return render(request,'sound_userview.html',{'soundadmin':sound})










 





