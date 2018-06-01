from django.contrib import admin
from .models import Team, Player, Coach, Match
from django.utils.safestring import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_rut', 'age', 'height', 'weight', 'thumb', )

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_rut', 'age','email','nickname',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('name','date')