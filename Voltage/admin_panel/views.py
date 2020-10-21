from django.shortcuts import render
from django.shortcuts import HttpResponse
from admin_panel.models import events
from admin_panel.models import reservations
from admin_panel.models import eventbin
from admin_panel.models import customer
from admin_panel.models import admin_login
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date
from datetime import datetime
import datetime
from django.utils import timezone
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.contrib.auth import logout
# from django.db.models.functions import ExtractYear
# from django.db.models.functions import ExtractMonth
# Create your views here.


def reservation_manage(request):
    
 eve = events.objects.all()
 eve1 = eventbin.objects.all()
 context = {'event' : eve, 'completed_events' : eve1}
 return render(request,'reservation_manage.html',context=context)





def review(request,id,user): 
 eve = events.objects.filter(Event_ID = id)
 res = reservations.objects.filter(Event_ID = id)
 user = customer.objects.filter(Customer_ID = 88) #temporary hardcoded value, Should be user
 event = events.objects.get(Event_ID = id)
 time =  (timezone.now() - event.OnCreateTime).total_seconds()/60.0
 diff = (2.0 - time)
 diffToString = str(diff)[0:5]
 if diff < 0:
     allow = 'you can confirm'
     messages.warning(request, 'Allowed time for update is over.')
     context = {'event' : eve, 'reservations' : res, 'customer' : user, 'allow':allow,'diff':diff}
     return render(request,'review.html',context=context)
 else:
   context = {'event' : eve, 'reservations' : res, 'customer' : user, 'diff':diff}
   messages.warning(request, 'Customer may update within  '+diffToString+'min')
   return render(request,'review.html',context=context)


def viewReservation(request,id,user): 
 eve = events.objects.filter(Event_ID = id)
 res = reservations.objects.filter(Event_ID = id)
 user = customer.objects.filter(Customer_ID = user)
 context = {'event' : eve, 'reservations' : res, 'customer' : user}
 return render(request,'admin_view.html',context=context)


def deleteReservation(request,id,user): 
 eve = eventbin.objects.filter(Event_ID = id)
 res = reservations.objects.filter(Event_ID = id)
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
    time =  (timezone.now() - event.OnCreateTime).total_seconds()/60.0
    if time > 2.0: #if time interval between event created time and current time is less than 1hour, admin cannot confirm
      event.Status = 'upcoming'
      event.save()
      return redirect(reservation_manage)

    else:
      messages.error(request, 'Please wait for the remaining time!')
      return redirect(request.META.get('HTTP_REFERER'))


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
           
           AdminID = admin_login.objects.filter(username = username, password=password).only('admin_id')[0].admin_id
           request.session['name'] = AdminID
           return redirect(AdminPanel)
       
       else:
            messages.warning(request, 'Invalid username or password')
            return redirect(request.META.get('HTTP_REFERER')) 
   
    else:
     return render(request,'admin_login.html')
 
 
def AdminPanel(request):
       admin_ID = request.session['name'] 
       user = admin_login.objects.filter(admin_id = admin_ID)
       eve = events.objects.filter(Status = 'upcoming').order_by('Date')[:3]
       context = {'event' : eve, 'admin_login' : user}
       return render(request,'admin_panel.html',context=context)
 
 
 
 
 
def sendmail(request):
    send_mail('Hello',
    'Your reservation has confirmed.We will Contact you soon.Thank you',
    'voltage.en@gmail.com',['udithaj.98@gmail.com'],
    fail_silently=False)
    messages.error(request, 'Email successfuly sent!')
    return redirect(request.META.get('HTTP_REFERER')) 


def getmonthlyreport(request):
    if request.method == 'POST':
          if request.POST.get('month'):
            getmonth = request.POST.get('month')
            converted_date = datetime.datetime.strptime(getmonth, "%Y-%m").date()
            year = converted_date.year
            month = converted_date.month
            eve = events.objects.filter(Date__year=year).filter(Date__month=month)
            ended = eventbin.objects.filter(Date__year=year).filter(Date__month=month)
            context = {'event':eve,'completed_events':ended,'getmonth':getmonth}
            template = get_template("main_report.html")
            context_r = template.render(context)
            response = BytesIO()
            
            pdfReport = pisa.pisaDocument(BytesIO(context_r.encode("UTF-8")),response)
            if not pdfReport.err:
                return HttpResponse(response.getvalue(),content_type ="application/pdf")
            else:
                return HttpResponse("Error generating Report")
          else:
             messages.warning(request, 'Please Enter the Month!')
             return redirect(AdminPanel)
     
        
    else:
        return render(request,'main_report.html')
    
    
    
    
def Adminlogout(request,id):
    

     print( request.session['name'])
     del request.session['name']
     return redirect(Adminlogin)
 

       