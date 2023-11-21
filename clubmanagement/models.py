from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name

class Match(models.Model):
    date = models.DateField()
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    result = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date}"