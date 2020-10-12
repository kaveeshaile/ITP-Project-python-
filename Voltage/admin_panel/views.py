from django.shortcuts import render
from admin_panel.models import events
from admin_panel.models import reservations
from admin_panel.models import eventbin
from admin_panel.models import customer
from admin_panel.models import admin_login
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

# def admin_panel(request):

#  return render(request,'admin_panel.html')
        

# def reservation_manage(request):
    
#  eve = eventbin.objects.all()
# #  eve1 = eventbin.objects.all()
#  return render(request,'reservation_manage.html',{'completed_events':eve})
#  print(eve)

def reservation_manage(request):
    
 eve = events.objects.all()
 eve1 = eventbin.objects.all()
 context = {'event' : eve, 'completed_events' : eve1}
 return render(request,'reservation_manage.html',context=context)





def review(request,id,user): 
 eve = events.objects.filter(Event_ID = id)
 res = reservations.objects.filter(Event_ID = 1)
 user = customer.objects.filter(Customer_ID = user)
 context = {'event' : eve, 'reservations' : res, 'customer' : user}
 return render(request,'review.html',context=context)


def viewReservation(request,id,user): 
 eve = events.objects.filter(Event_ID = id)
 res = reservations.objects.filter(Event_ID = 1)
 user = customer.objects.filter(Customer_ID = user)
 context = {'event' : eve, 'reservations' : res, 'customer' : user}
 return render(request,'admin_view.html',context=context)


def deleteReservation(request,id,user): 
 eve = eventbin.objects.filter(Event_ID = id)
 res = reservations.objects.filter(Event_ID = 1)# temporary value
 user = customer.objects.filter(Customer_ID = user)
 context = {'completed_events' : eve, 'reservations' : res, 'customer' : user}
 return render(request,'admin_delete.html',context=context)


def DeleteEvent(request,id):
    event = eventbin.objects.filter(Event_ID = id)
    res = reservations.objects.filter(Event_ID=id)
    event.delete()
    res.delete()
    return redirect(reservation_manage) 

def ConfirmEvent(request,id):
    event = events.objects.get(Event_ID = id)
    event.Status = 'upcoming'
    event.save()
    return redirect(reservation_manage) 


def MarkAsCompleted(request,id):
    event = events.objects.get(Event_ID = id)
    event.Status = 'completed'
    event.save()
    return redirect(reservation_manage) 


def Adminlogin(request):
    if request.method =='POST':
       username =  request.POST.get('username')
       password = request.POST.get('password')
       
       if admin_login.objects.filter(username = username, password=password):
           
           user = admin_login.objects.filter(username = username, password=password)
           AdminID = [item.admin_id for item in user]
           AdminID = str(AdminID)[1:-1]  #remove [] from result
           print(AdminID)
           request.session['name'] = AdminID
           eve = events.objects.filter(Status = 'upcoming')
           context = {'event' : eve, 'admin_login' : user}
           return render(request,'admin_panel.html',context=context)
       
       else:
            messages.warning(request, 'Invalid username or password')
            return redirect(request.META.get('HTTP_REFERER')) 
   
    else:
     return render(request,'admin_login.html')
 
 
 
 
def sendmail(request):
    send_mail('hello',
    'your reservation has confirmed',
    'voltage.en@gmail.com',
    ['begaheh976@justlibre.com'],
    fail_silently=False)
    return render(request,'admin_login.html')