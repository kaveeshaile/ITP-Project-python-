from django.shortcuts import render

# Create your views here.

def admin_panel(request):return render(request,'admin_panel.html')

def reservation_manage(request):return render(request,'reservation_manage.html')

def review(request):return render(request,'review.html')