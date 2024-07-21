# -*- coding: utf-8 -*-
from constants import *
import player


class TennisGame():
    def __init__(self, player1_points, player2_points, player1_name, player2_name):
        self.language = "fr"
        self.player2_won = False
        self.is_player2_up = False
        self.Player1 = player.Player(player1_name)
        self.Player2 = player.Player(player2_name)
        self.player2_points = player2_points
        self.player1_points = player1_points
        self.player1_won = False
        self.someone_won = False
        self.is_advantage_situation = False

        self.is_player1_up = False
        self.are_scores_equal = False
        self.player2_up_by = 0
        self.player1_up_by = 0

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
        if self.player1_won or self.player2_won:
            return self.score_with_victory()
        # en situation normale
        if not self.are_scores_equal:
            return self.score_normal()

    def score_with_advantage(self):
        return ADVANTAGE_PLAYER1 if self.player1_up_by == 1 else ADVANTAGE_PLAYER2

    def score_with_equality(self):
        return equality_table[self.player1_points] if self.player1_points < 3 else equality_table[3]

    def score_with_victory(self):
        return winners["player1"] if self.player1_won else winners["player2"]

    def score_normal(self):
        return scores_text[self.player1_points] + "-" + scores_text[self.player2_points]

    def run_pre_game_checks(self):
        #equality
        self.are_scores_equal = True if self.player1_points == self.player2_points else False
        self.is_player1_up = True if self.player1_points - self.player2_points > 0 else False
        self.is_player2_up = True if self.player2_points - self.player1_points > 0 else False
        self.player1_up_by = self.player1_points - self.player2_points if self.is_player1_up else 0
        self.player2_up_by = self.player2_points - self.player1_points if self.is_player2_up else 0
        self.player1_won = True if self.player1_points > 3 and self.player1_up_by >= 2 else False
        self.player2_won = True if self.player2_points > 3 and self.player2_up_by >= 2 else False
        self.is_advantage_situation = True if (self.player1_points >= 3 and self.player2_points >= 3) and (
        self.player1_up_by == 1 or self.player2_up_by == 1) else False

