class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.games = dict['games']
        self.id = dict['id']


    def score(self):
        return self.goals + self.assists

    
    def __str__(self):
        pisteet = int(self.goals) + int(self.assists)
        
        return f"{self.name:<20} {self.team}  {self.goals} + {self.assists} = {pisteet}"