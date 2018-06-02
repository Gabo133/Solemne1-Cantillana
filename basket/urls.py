from django.urls import path
from basket import views


urlpatterns = [

    path('',views.list_match, name="match"),
    path('index', views.index, name="index"),

    path('index_super', views.index, name="index"),

    path('list_player', views.list_player, name="list_player"),
    path('list_coach', views.list_coach, name="list_coach"),
    path('list_team', views.list_team, name="list_team"),
    path('list_match', views.list_match, name="list_match"),


    path('add_player', views.add_player, name="add_player"),
    path('add_coach', views.add_user, name="add_coach"),
    path('add_user', views.add_coach, name="add_user"),

    path('add_team', views.add_team, name="add_team"),
    path('add_match', views.add_match, name="add_match"),


    path('edit_player/<int:player_id>', views.edit_player, name="Player_edit"),
    path('edit_team/<int:team_id>', views.edit_team, name="Team_edit"),
    path('edit_coach/<int:coach_id>', views.edit_coach, name="Coach_edit"),

    path('delete/<int:id>', views.Delete, name="Delete"),
]