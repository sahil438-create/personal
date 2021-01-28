from django.urls import path
from . import views

urlpatterns = [
    
    
    path('',views.blo,name='blo'),
    path('<int:blog>',views.detail ,name='detail'),
    
    
    
]