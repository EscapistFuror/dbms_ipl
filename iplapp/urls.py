from django.urls import path
from . import views

urlpatterns = [
    path('', views.Team_List, name='Team_List'),
    path('Player_List/', views.Player_List, name='Player_List'),
    path('update_player',views.update_player,name='update_player'),

]
