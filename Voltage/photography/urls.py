from django.urls import path
from.import views

urlpatterns = [
    path('', views.photo_add, name='photo_add')
]

urlpatterns = [
    path('', views.photo_update, name='photo_update')
]
