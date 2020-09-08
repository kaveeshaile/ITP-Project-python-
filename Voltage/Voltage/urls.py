"""Voltage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
<<<<<<< HEAD
=======
    path('', include('soundsystems.urls')),
    path('', include('videography.urls')),
>>>>>>> 3622a117c74b5affba31adf59a2c3fd9907029ca
    path('', include('admin_panel.urls')),
    path('', include('videography.urls')),
    path('', include('home.urls')),
    path('', include('photography.urls')),
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
     path('', include('payment.urls')),
>>>>>>> 98aaf075acd870d7f858b6bcbf2a4ea5579c58ef
    path('admin/', admin.site.urls),
  
=======
    path('', include('photo_checkdelete.urls')),
    path('', include('customer_main.urls')),
    path('', include('photo_add.urls')),
    path('', include('photo_update.urls')),
    path('', include('music_band.urls')),


>>>>>>> Stashed changes

]
