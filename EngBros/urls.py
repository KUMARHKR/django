from django.urls import path
from EngBros import views

urlpatterns = [
   
   path("",views.index,name='EngBros'),
   path("inpage",views.inpage,name='EngBros'),
   path("portfolio",views.portfolio,name='EngBros'),
     path("graphic",views.graphic,name='EngBros')
   
]