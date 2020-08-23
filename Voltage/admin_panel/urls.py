from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.review,name = 'review'),
    path('',views.reservation_manage,name = 'reservation_manage'),
    path('',views.admin_panel,name = 'admin_panel')
   

    
]

