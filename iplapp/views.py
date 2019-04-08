from django.http import HttpResponse
from django.shortcuts import render
from .models import Team,Player,Sold_Players
# Create your views here.
def Team_List(request):
    Teams=Team.objects.all()
    return render(request, 'iplapp/Team_List.html', {'Teams' : Teams})

def Player_List(request):
    Players=Player.objects.all()
    id2=0
    return render(request, 'iplapp/Player_List.html',{'Players' : Players,'id2': id2})

def update_player(request):
    p=Player.objects.all()
    name= request.POST["name"]
    id1=request.POST["id1"]
    id2=int(id1)+1
    bid_price= request.POST["bid_price"]
    TName= request.POST["TName"]
    sname=Player.objects.get(name=name)
    tname=Team.objects.get(TName=TName)
    s_p=Sold_Players(name=sname,bid_price=int(bid_price),TName=tname)
    s_p.save()
    # Players=[]
    x=int(tname.player_count)
    tname.player_count=x+1
    y=int(tname.balance)
    tname.balance=y-int(bid_price)
    tname.save()
    Players=Player.objects.all()
    # Players = Player.objects.filter(int(Player.pk)>int(id1))
    # /return HttpResponse("return this string")
    return render(request, 'iplapp/Player_List.html', {'Players': Players,'id2': id2})
