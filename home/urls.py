from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    
    
   
 
    #path('userform',views.userform),
   # path('calculator',views.calculator),
    path('practice/<slug>',views.practice),
    path('we/',views.we,name='we'),
    path('us/<id>',views.us,name='us'),
    path('second/',views.second)

    
    

    
]