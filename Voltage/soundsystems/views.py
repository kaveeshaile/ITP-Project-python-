from django.shortcuts import render




def sound_userview(request): return render(request, 'sound_userview.html')

def sound_main(request): return render(request, 'sound_main.html')

def sound_admin_upload(request): return render(request, 'sound_admin_upload.html')

def sound_update(request): return render(request, 'sound_update.html')





