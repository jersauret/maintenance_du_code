import os
import unittest

class GoldenMasterTest(unittest.TestCase):
    Dir = os.path.join(os.path.expanduser("~"), "Source", "Repos", "Tennis-Refactoring-Kata", "csharp", "Tennis.Tests", "golden-master")

    @staticmethod
    def cas_golden_master():
        for score_player1 in range(21):
            for score_player2 in range(21):
                yield "player1", "player2", score_player1, score_player2
                yield "player2", "player1", score_player1, score_player2
                yield "", "player1", score_player1, score_player2
                yield "player1", "", score_player1, score_player2

    def record(self, name_of_first_player, name_of_second_player, score_player1, score_player2):
        try:
            game = TennisGame3(name_of_first_player, name_of_second_player)
            result = self.check_all_scores(game, score_player1, score_player2)
        except Exception as e:
            result = type(e).__name__ + " " + str(e)

        file_name = f"{score_player1}-{score_player2}-{name_of_first_player}-{name_of_second_player}.txt"
        with open(os.path.join(self.Dir, file_name), "w") as f:
            f.write(result)

    def replay(self, name_of_first_player, name_of_second_player, score_player1, score_player2):
        try:
            game = TennisGame3(name_of_first_player, name_of_second_player)
            result = self.check_all_scores(game, score_player1, score_player2)
        except Exception as e:
            result = type(e).__name__ + " " + str(e)

        file_name = f"{score_player1}-{score_player2}-{name_of_first_player}-{name_of_second_player}.txt"
        with open(os.path.join(self.Dir, file_name), "r") as f:
            expected = f.read()

        self.assertEqual(expected, result)

    def check_all_scores(self, game, player1_score, player2_score):
        highest_score = max(player1_score, player2_score)
        for i in range(highest_score):
            if i < player1_score:
                game.won_point("player1")
            if i < player2_score:
                game.won_point("player2")

        return game.get_score()
