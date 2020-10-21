from django.urls import path
from.import views



urlpatterns = [ 


      path('sound_test',views.sound_display_admin,name = 'sound_display_admin'),
      path('sound_userview',views.display_customers,name = 'display_customers'),
      path('sound_test/<id>',views.edit,name = 'edit'),
      path('sound_test2',views.sound_admin_update,name = 'sound_admin_update'),
      path('sound_test2/<id>',views.sound_delete,name = 'sound_delete'),
      path('sound_admin_upload',views.sound_insert,name = 'sound_insert'),
      
      
     
     
  
    
]
                

   
    
               
