from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from graphicdesign.models import gdInsert
from django.shortcuts import get_object_or_404


def Add(request):
     if request.method=='POST':
        if  request.POST.get('idgraphicdesignID')   and request.POST.get('graphicname') and request.POST.get('graphicfee') and request.POST.get('graphicdec') and request.POST.get('graphicconatact') and request.POST.get('graphicemail'):
           graph=gdInsert()
           
           graph.idgraphicdesignID=request.POST.get('idgraphicdesignID')
           graph.graphicname=request.POST.get('graphicname')
           graph.graphicfee=request.POST.get('graphicfee')
           graph.graphicdec=request.POST.get('graphicdec')
           graph.graphiccontact=request.POST.get('graphiccontact')
           graph.graphicemail=request.POST.get('graphicemail')
           graph.save()
           return redirect(displayall)
     else:
           return render(request, 'graph_add.html')

def displayall(request):
           graphicdesign = gdInsert.objects.all()
           return render(request,'graph_RecentlyAdd.html',{'graphicdesign':graphicdesign})

def displayall2(request):
           graphicdesign = gdInsert.objects.all()
           return render(request,'graph_reservations.html',{'graphicdesign':graphicdesign})

def RemoveGraphic(request,id):
           graphicdesign = gdInsert.objects.filter(id=id)
           graphicdesign.delete()
           return redirect(displayall)


def UpdateGraphic(request):
     if request.method=='POST':
        if  request.POST.get('graph_name'):   
           graph=gdInsert.objects.get(id=id)
           id=request.POST.get('id')
           graph.idgraphicdesignID=request.POST.get('idgraphicdesignID')
           graph.graphicname=request.POST.get('graphicname')
           graph.graphicfee=request.POST.get('graphicfee')
           graph.graphicdec=request.POST.get('graphicdec')
           graph.graphiccontact=request.POST.get('graphiccontact')
           graph.graphicemail=request.POST.get('graphicemail')
           graph.save()
        return redirect(displayall)
     else:
        return render(request, 'graph_add.html')
