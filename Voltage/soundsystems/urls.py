from django.urls import path
from.import views


urlpatterns = [ 


      path('',views.sound_admin_upload,name = 'sound_admin_upload'),
      path('',views.sound_main,name = 'sound_main')
    
    
    
    
]
                

   
    
               
