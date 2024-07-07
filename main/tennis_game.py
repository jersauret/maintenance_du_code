# -*- coding: utf-8 -*-


class TennisGame1():
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        # consistence de nommage player1name vs p1
        self.p1points = 0
        self.p2points = 0
        # objet pour comprendre le métier

    def won_point(self, playerName):
        # fonction mal nommée diff avec action réele: increment player point
        if playerName == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore=0
        if (self.p1points==self.p2points):
            result = {
                # Fichier de constantes !! mal écrit
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce") # Fichier de constantes !!
            # boucle imbriquée
            # pour gérer le flow du jeu
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            if (minusResult==1):
                result ="Advantage player1"
            elif (minusResult ==-1):
                result ="Advantage player2"
            elif (minusResult>=2):
                result = "Win for player1"
            else:
                result ="Win for player2"
                # constante magigue
                # explication du ouquoi + fonctions
        else:
            for i in range(1,3): # 1 a 3 ??? Constante à utiliser
                if (i==1):
                    # Logique incompréhensible
                    tempScore = self.p1points
                else:
                    result+="-"
                    # si c'est typé sinon erreur
                    tempScore = self.p2points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        return result
