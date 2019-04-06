from django.contrib import admin
from .models import Team,Player,Sold_Players

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Sold_Players)