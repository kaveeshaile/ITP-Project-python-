from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.displayall,name = 'displayall'),
    path('',views.displaytocustomer,name = 'displayvideo'),
    path('video_add',views.addvideo,name = 'addvideo')
]

