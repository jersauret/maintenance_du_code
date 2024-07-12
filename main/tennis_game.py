# -*- coding: utf-8 -*-
from constants import *
import player

class TennisGame():
    def __init__(self,player1_points, player2_points, player1_name, player2_name):
        self.is_advantage_situation = None
        
        self.is_player1_up = None
        self.are_scores_equal = None
        self.player2_up_by = None
        self.player1_up_by = None
        self.Player1 = player.Player(player1_name)
        self.Player2 = player.Player(player2_name)
        self.Player1.update_score_from_number(player1_points)
        self.Player2.update_score_from_number(player2_points)
    
    def get_current_score_display(self):
        #faisons toutes les verifications sur les scores etc
        self.run_pre_game_checks()
        # GERONS LES DIFFERENTES SITUATIONS
        # en situation d'égalité (situation de départ)
        if self.are_scores_equal:
            return self.score_with_equality()        
        # en situation d'avantage
        if self.is_advantage_situation:
            return self.score_with_advantage()
        # en situation de victoire
        if self.someone_won:
            return self.score_with_victory()
        # en situation normale
        return self.score_normal()

    def score_with_advantage(self):
        return ADVANTAGE_PLAYER1 if self.player1_up_by ==1 else ADVANTAGE_PLAYER2
    def score_with_equality(self):
        return equality_table[self.Player1.get_score_as_number]
    def score_with_victory(self):
        return winners["player1"] if self.player1_won else winners["player2"]
    def score_normal(self):
        return self.Player1.get_score_as_text + "-" + self.Player2.get_score_as_text
    def run_pre_game_checks(self):
        player1_points = self.Player1.get_score_as_number()
        player2_points = self.Player2.get_score_as_number()
        self.player1_up_by = player1_points - player2_points if player1_points - player2_points > 0 else 0
        self.player2_up_by = player2_points - player1_points if player2_points - player1_points > 0 else 0
        self.are_scores_equal = True if player1_points == player2_points else False
        self.is_player1_up = True if player1_points - player2_points > 0 else False
        self.someone_won = True if self.player1_up_by == 2 or self.player2_up_by == 2 else False
        self.is_advantage_situation = True if (player1_points > 3 and player2_points > 3) and (self.player1_up_by == 1 or self.player2_up_by == 1) else False
        self.player1_won = True if self.player1_up_by == 2 else False