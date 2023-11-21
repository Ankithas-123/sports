from django.urls import path
from .views import PlayerListView, TeamListView, MatchListView
from clubmanagement.views import AllDataView

urlpatterns = [
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('matches/', MatchListView.as_view(), name='match-list'),
    path('all_data/', AllDataView.as_view(), name='all-data'),
    #club/matches/--------

]