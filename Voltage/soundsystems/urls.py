from django.urls import path
from.import views



urlpatterns = [ 

      path('',views.sound_admin_update,name = 'sound_admin_update'),
      path('',views.sound_insert,name = 'sound_insert'),
      path('',views.sound_userview,name = 'sound_userview'),
      path('',views.sound_main,name = 'sound_main')
   
   
    
]
                

   
    
               
