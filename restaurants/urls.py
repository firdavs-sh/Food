from django.urls import path
from .views import *

urlpatterns = [
    path('mahsulotlar/', RestaurantListView.as_view(), name='mahsulotlar'),
    path('create/', RestaurantCreateView.as_view(), name='create'),
    path("about/",about,name="about"),
    path('<slug:slug>/', RestaurantDetailView.as_view(), name='detail'),
    path("",index,name="index"),
  
   
]
