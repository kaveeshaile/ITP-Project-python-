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
            #return render(request,'sound_admin_upload.html')
            return render(request,'sound_admin_upload.html')
    
    


def sound_admin_update(request):

   if request.method == "POST":
        if request.POST.get('id'):
         id =  request.POST.get('id')
         sound = sound_admin.objects.get(id = id)
         print(sound)
         sound.Package_name =  request.POST.get('packname')
         sound.Suitable_for =  request.POST.get('suitable')
         sound.Brand =  request.POST.get('brand')
         sound.Price =  request.POST.get('price')
         sound.save()
         #return redirect(sound_display_admin)

     #     return redirect('/') 
         return render(request,'sound_admin_upload.html')
         #context = {'sound_admin': sound}
         #return render(request,'sound_test2.html',{'soundadmin':sound})
        
   else:
      
         return render(request,'sound_admin_upload.html')
     






def sound_display_admin(request):
   
     sound = sound_admin.objects.all();
     #context = {'sound_admin': sound}
     return render(request,'sound_test.html',{'soundsystem':sound})
     #return render(request,'sound_test.html', context=context)



def edit(request,id):

    #if request.method == "POST":
     #id =  request.POST.get('id')
     sound = sound_admin.objects.filter(id=id)
     #context = {'sound_admin': sound}
     #return render(request, 'sound_test2.html', context=context)
     #return render(request,'sound_test2.html',{'soundadmin':sound})
     
     return render(request,"sound_test2.html",{"soundsystem":sound})

    




def display_customers(request):
    
     sound = sound_admin.objects.all();
     #context = {'sound_admin': sound_admin}

     return render(request,'sound_userview.html',{'soundsystem':sound})



def sound_delete(request, id):
    sound = sound_admin.objects.filter(id=id)
    sound.delete()
    return render(request,'sound_admin_upload.html')






 





