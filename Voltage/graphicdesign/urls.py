from django.urls import path
from.import views
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.displayall,name = 'displayall'),
    path('graph_add',views.Add,name = 'Add'),
    path('graph_RecentlyAdd',views.displayall,name = 'displayall'),
    path('graph_delete/<id>',views.RemoveGraphic,name = 'RemoveGraphic'),
    path('graph_Update',views.UpdateGraphic,name = 'UpdateGraphic')


   
    
]
                

   
    
               
