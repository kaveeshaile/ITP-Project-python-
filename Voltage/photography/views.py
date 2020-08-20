from django.shortcuts import render

# Create your views here.


def photo_add(request): return render(request, 'photo_add.html')


def photo_update(request): return render(request, 'photo_update.html')
