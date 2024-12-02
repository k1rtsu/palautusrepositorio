class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.p1 = player1_name
        self.p2 = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def score_types(self, game:int):
        types = ["Love","Fifteen","Thirty","Forty"]
        return types[game]

    def won_point(self, player_name):
        if player_name == self.p1:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.tie_score()
        elif self.p1_score >= 4 or self.p2_score >=4:
            return self.lastpoint_score()
        
        return self.normal_score()
    
    def tie_score(self):
        if self.p1_score < 3:
            return f'{self.score_types(self.p1_score)}-All'
        
        return f'Deuce'
    
    def lastpoint_score(self):
        dif = self.p1_score - self.p2_score

        if dif == 1:
            return 'Advantage player1'
        if dif  == -1:
            return 'Adventage player2'
        if dif >= 2:
            return 'Win for player1'
        
        return 'Win for player2'
    
    def normal_score(self):
        p1 = self.score_types(self.p1_score)
        p2 = self.score_types(self.p2_score)
        return f'{p1}-{p2}'
