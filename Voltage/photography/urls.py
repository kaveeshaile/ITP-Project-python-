from django.urls import path
from.import views

urlpatterns = [
    path('photo_add', views.photo_add, name='photo_add'),
    path('', views.photo_update, name='photo_update'),
    path('customer_main', views.customer_main, name='customer_main'),
    path('', views.photo_checkdelete, name='photo_checkdelete'),
    path('', views.photo_profile, name='photo_profile')
]
