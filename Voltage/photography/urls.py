from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from.import views
# upload file

urlpatterns = [



    path('addPhoto', views.addPhoto, name='addPhoto'),
    path('displayone', views.displayone, name='displayone'),
    path('delete/<id>', views.admindelete, name='admindelete'),
    path('GetDetailsForUpdate/<id>', views.GetDetailsForUpdate,
         name='GetDetailsForUpdate'),

    path('update/<id>', views.AdminUpdate, name='AdminUpdate'),
<<<<<<< HEAD
    # path('customer_main', views.displayall, name='displayall'),
    # path('photo_profile', views.bookphotographer, name='bookphotographer'),
=======
    path('customer_main', views.displaycustomer, name='displaycustomer'),
    path('photo_profile', views.bookphotographer, name='bookphotographer'),
>>>>>>> 729c4437678e5ba9bc486796cb797c67421f7825
    path('customer_main/<id>', views.photoprofile, name='photoprofile'),
    path('Photo_admin_display', views.getmonthlyreportforphotographer,
         name='getmonthlyreportforphotographer')
]
