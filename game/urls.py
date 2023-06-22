from django.urls import path
from game.views import Restaurant1ListView, Restaurant1DetailView,reklama,g1,g2,g3,g4,g5,g6,gbase

urlpatterns = [
    path("gbase/",gbase,name="gbase"),
    path("g1/",g1,name="g1"),
    path("g2/",g2,name="g2"),
    path("g3/",g3,name="g3"),
    path("g4/",g4,name="g4"),
    path("g5/",g5,name="g5"),
    path("g6/",g6,name="g6"),
    path('music/', Restaurant1ListView.as_view(), name='music1'),
    path('<slug:slug>/', Restaurant1DetailView.as_view(), name='game'),
  

]
