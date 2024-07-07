# -*- coding: utf-8 -*-


class TennisGame():
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        # consistence de nommage player1name vs p1
        self.player1_points = 0
        self.player2_points = 0
        # objet pour comprendre le métier

    def won_point(self, player_name):
        # fonction mal nommée diff avec action réele: increment player point
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        result = ""
        temp_score = 0
        if (self.player1_points == self.player2_points):
            result = {
                # Fichier de constantes !! mal écrit
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")  # Fichier de constantes !!
            # boucle imbriquée
            # pour gérer le flow du jeu
        elif self.player1_points >= 4 or self.player2_points >= 4:
            minus_result = self.player1_points - self.player2_points
            if minus_result == 1:
                result = "Advantage player1"
            elif minus_result == -1:
                result = "Advantage player2"
            elif minus_result >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
                # constante magigue
                # explication du ouquoi + fonctions
        else:
            for i in range(1, 3):  # 1 a 3 ??? Constante à utiliser
                if (i == 1):
                    # Logique incompréhensible
                    temp_score = self.player1_points
                else:
                    result += "-"
                    # si c'est typé sinon erreur
                    temp_score = self.player2_points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
