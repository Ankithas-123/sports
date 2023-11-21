from django.shortcuts import render
from django.views import View
from .models import Player, Team, Match

class PlayerListView(View):
    def get(self, request):
        players = Player.objects.all()
        return render(request, 'player_list.html', {'players': players})

class TeamListView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'team_list.html', {'teams': teams})

class MatchListView(View):
    def get(self, request):
        matches = Match.objects.all()
        return render(request, 'match_list.html', {'matches': matches})


class AllDataView(View):
    def get(self, request):
        players = Player.objects.all()
        teams = Team.objects.all()
        matches = Match.objects.all()
        return render(request, 'all_data.html', {'players': players, 'teams': teams, 'matches': matches})
