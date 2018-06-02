from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('list', views.index, name="player_list"),
    path('add_player', views.add_player, name="player_add"),
    path('add_coach', views.add_coach, name="Coach_add"),
    path('add_team', views.add_team, name="Team_add"),
    path('add_match', views.add_match, name="Match_add"),
    path('edit_player/<int:player_id>', views.edit_player, name="Player_edit"),
    path('edit_team/<int:team_id>', views.edit_team, name="Team_edit"),
    path('edit_coach/<int:coach_id>', views.edit_coach, name="Coach_edit"),
    path('delete/<int:id>', views.Delete, name="Delete"),
]