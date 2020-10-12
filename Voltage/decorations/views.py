from django.shortcuts import render
from decorations.models import decorationInsert
from django.contrib import messages
# Create your views here.

def Add(request):
     if request.method=='POST':
        if request.POST.get('dec_name') and 
           request.POST.get('dec_dsc') and
           request.POST.get('dec_img1') and
           request.POST.get('dec_img2') and
           request.POST.get('dec_img3') and
           request.POST.get('dec_img4') and
           request.POST.get('dec_img5'):
           saverecord=decorationInsert()
           saverecord.dec_name=request.POST.get('dec_name')
           saverecord.dec_dsc=request.POST.get('dec_dsc')
           saverecord.dec_img1=request.POST.get('dec_img1')
           saverecord.dec_img2=request.POST.get('dec_img2')
           saverecord.dec_img3=request.POST.get('dec_img3')
           saverecord.dec_img4=request.POST.get('dec_img4')
           saverecord.dec_img5=request.POST.get('dec_img5')
           saverecord.save()
           messages.success(request, 'Succcess')
           return render(request, 'dec_add.html')
    else:
           return render(request, 'dec_add.html')
