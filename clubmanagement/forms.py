from django import forms
from .models import Player, Team

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'position']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'players']