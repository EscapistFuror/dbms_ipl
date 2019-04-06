from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.Team_List, name='Team_List'),
    path('Player_List/', views.Player_List, name='Player_List'),

]
