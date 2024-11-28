class TennisGame:
    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        match player_name:
            case self.p1_name:
                self.p1_score += 1
            case self.p2_name:
                self.p2_score += 1

    def get_score(self):
        points = ["Love", "Fifteen", "Thirty", "Forty"]

        if self.p1_score == self.p2_score:

            if self.p1_score >= 3:
                return "Deuce"
            return points[self.p1_score] + "-All"
        
        elif self.p1_score >= 4 or self.p2_score >= 4:

            diff = self.p1_score - self. p2_score
            state = "Advantage " if abs(diff) == 1 else "Win for "
            player = self.p1_name if diff > 0 else self.p2_name
            return state + player
        
        else:

            return points[self.p1_score] + "-" + points[self.p2_score]
