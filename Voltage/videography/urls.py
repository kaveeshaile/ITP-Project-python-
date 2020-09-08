from django.urls import path
from.import views

urlpatterns = [

    path('display_all_vid',views.displayall,name = 'displayall'),
    path('video_add',views.addvideo,name = 'addvideo'),
    path('',views.displaytocustomer,name = 'displayvideo')

]

