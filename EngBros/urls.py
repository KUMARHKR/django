from django.urls import conf, path
from EngBros import views


urlpatterns = [
   
   path("",views.index,name='EngBros'),
   path("inpage",views.inpage,name='EngBros'),
   path("portfolio",views.portfolio,name='EngBros'),
   path("graphic",views.graphic,name='EngBros'),
   path("webdev",views.webdev,name='EngBros'),
   path("seo",views.seo,name='EngBros'),
   path("digitalmarketing",views.digitalmarketing,name='EngBros'),
   
]
