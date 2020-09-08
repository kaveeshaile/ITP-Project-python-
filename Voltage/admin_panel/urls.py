from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.admin_panel,name = 'admin_panel'),
    path('review',views.review,name = 'review'),
    path('reservation_manage',views.reservation_manage,name = 'reservation_manage')
    
]

