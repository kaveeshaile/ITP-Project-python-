from django.urls import path,re_path
from.import views

urlpatterns = [
    #path('video_profile',views.displaytocustomer,name = 'displayvideo'),
    path('video_add',views.addvideo,name = 'addvideo'),
    path('video_recently_added',views.displayAlltoAdmin,name = 'displayAlltoAdmin'),
    path('video_recently_added/<id>',views.displayProfiletoAdmin,name = 'displayProfiletoAdmin'),
    path('video_customer_main',views.displayall,name = 'displayall'),
    path('video_customer_main/<id>',views.VideographerProfile,name = 'VideographerProfile'),
    path('video_update/<id>',views.RemoveVideoGrapher,name = 'RemoveVideoGrapher'),
    path('video_update',views.UpdateVideoGrapher,name = 'UpdateVideoGrapher'),
    path('video_profile',views.bookVideographer,name = 'bookVideographer'),
    path('event_create',views.CreateEvent,name = 'CreateEvent'),
    path('main_reservation_page',views.submitEvent,name = 'submitEvent'),
    path('main_reservation_page/<id>',views.CancelEvent,name = 'CancelEvent')
    
    
    

]

