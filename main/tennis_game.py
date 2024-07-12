from constants import scores


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        # consistence de nommage player1name vs p1
        self.player1_points = 0
        self.player2_points = 0
        # objet pour comprendre le métier

    def increment_player_points(self, player_name):
        # fonction mal nommée diff avec action réele: increment player point
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        score_in_text = ""
        if self.player1_points == self.player2_points:
            if self.player1_points == 0:
                return scores["LOVE_ALL"]
            if self.player1_points == 1:
                return scores["FIFTEEN_ALL"]
            if self.player1_points == 2:
                return scores["THIRTY_ALL"]
            if self.player1_points == 3:
                return scores["DEUCE"]
        elif self.player1_points >= 4 or self.player2_points >= 4:
            minus_result = self.player1_points - self.player2_points
            if minus_result == 1:
                score_in_text = "Advantage player1"
            elif minus_result == -1:
                score_in_text = 'Advantage player2'
            elif minus_result >= 2:
                score_in_text = "Win for player1"
            else:
                score_in_text = "Win for player2"
                # constante magigue
                # explication du ouquoi + fonctions
        else:
            for i in range(1, 3):  # 1 a 3 ??? Constante à utiliser
                if (i == 1):
                    # Logique incompréhensible
                    tempScore = self.player1_points
                else:
                    score_in_text += "-"
                    # si c'est typé sinon erreur
                    tempScore = self.player2_points
                score_in_text += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]
        return score_in_text
