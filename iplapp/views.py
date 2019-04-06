from django.shortcuts import render
from .models import Team,Player
# Create your views here.

def Team_List(request):
    Teams=Team.objects.all()
    return render(request, 'iplapp/Team_List.html', {'Teams' : Teams})

def Player_List(request):
    Players=Player.objects.all()
    return render(request, 'iplapp/Player_List.html',{'Players' : Players})

