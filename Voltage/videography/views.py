from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def video_add(request):return render(request,'video_add.html')