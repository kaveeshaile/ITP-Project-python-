from django.urls import path
from.import views

urlpatterns = [
    
    # path('admin_panel',views.admin_panel,name = 'admin_panel'),
    path('review/<id>/<user>',views.review,name = 'review'),
    path('reservation_manage',views.reservation_manage,name = 'reservation_manage'),
    path('admin_view/<id>/<user>',views.viewReservation,name = 'viewReservation'),
    path('admin_delete/<id>/<user>',views.deleteReservation,name = 'deleteReservation'),
    path('admin_delete/<id>',views.DeleteEvent,name = 'DeleteEvent'),
    path('review/<id>',views.ConfirmEvent,name = 'ConfirmEvent'),
    path('admin_view/<id>',views.MarkAsCompleted,name = 'MarkAsCompleted'),
    path('admin_login',views.Adminlogin,name = 'Adminlogin'),
    path('review',views.sendmail,name = 'sendmail'),
    path('main_report',views.getmonthlyreport, name = 'getmonthlyreport')
    
]

