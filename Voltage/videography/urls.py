from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.displaytocustomer,name = 'displayvideo'),
    path('video_add',views.addvideo,name = 'addvideo')
]

