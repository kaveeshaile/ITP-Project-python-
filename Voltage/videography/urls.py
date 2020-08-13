from django.urls import path
from.import views

urlpatterns = [
    path('',views.video_add,name = 'video_add')
]

